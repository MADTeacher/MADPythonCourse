from openpyxl.worksheet.worksheet import Worksheet

from document_settings import StructParse, DAY_OFF_COUNT
from parsers.parser import ScheduleParser
from schedule.daily_schedule import DailySchedule
from schedule.group import GroupInfo


class ScheduleBuilder:

    def __init__(self, worksheet: Worksheet):
        self.parser: ScheduleParser = ScheduleParser(worksheet)

    def build(self):
        group_schedule_list: list[GroupInfo] = []
        data_prapare_list = self.__prepare_data()
        for it in data_prapare_list:
            pre_schedule_data = self.parser.parse_schedule(it)
            group_schedule = GroupInfo(it[2][2])
            for key, info in enumerate(pre_schedule_data):
                day = DailySchedule(key+1)
                day_off_count = 0
                for it_lessons in info:
                    if it_lessons[1] == 'None':
                        day_off_count += 1
                    else:
                        day.lessons.append(it_lessons)
                if day_off_count >= DAY_OFF_COUNT:
                    day.day_off = True
                group_schedule.set_week_schedule(day)
            group_schedule_list.append(group_schedule)
        return self.__convert_to_dict(group_schedule_list)

    def __convert_to_dict(self, group_info: list[GroupInfo]):
        result_dict = {}
        for it in group_info:
            result_dict[it.name] = {}
            for key, itl in it.week_schedule.items():
                day_info_list = []
                if itl.day_off is True:
                    day_info_list.append('Выходной')
                else:
                    for lesson in itl.lessons:
                        if lesson[1] == 'None':
                            continue
                        day_info_list.append(f"<b>{lesson[0]}</b> {lesson[1]} <b>[</b>{lesson[2]}<b>]</b>")
                result_dict[it.name][key] = day_info_list
        return result_dict

    def __prepare_data(self):
        header_parse_list = self.parser.parse_header()
        data_prepare_list = []
        elem_split_list = []
        for it in header_parse_list:
            elem_split_list.append(it)
            if it[1] is StructParse.NumberClass:
                data_prepare_list.append(elem_split_list[:])
                elem_split_list = []

        temp = data_prepare_list[0]
        for it in data_prepare_list:
            if len(it) > 2:
                temp = it
            else:
                it.extend(temp[:2])
                it.sort(key=lambda x: x[1])
        return data_prepare_list
