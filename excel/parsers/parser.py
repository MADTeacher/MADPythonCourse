from openpyxl.worksheet.worksheet import Worksheet

from parsers.lessons_parser import LessonsParser
from parsers.time_parser import TimeParser
from parsers.classroom_parser import ClassroomParser
from document_settings import (START_PARSE_COL,
                               HEADER_ROW,
                               TIME_SPLIT_DATA,
                               CLASS_SPLIT_DATA,
                               DAY_SPLIT_DATA,
                               StructParse)


class ScheduleParser:

    def __init__(self, worksheet: Worksheet):
        self.worksheet = worksheet
        self.__time_parser = TimeParser(worksheet)
        self.__lessons_parser = LessonsParser(worksheet)
        self.__classroom_parser = ClassroomParser(worksheet)

    def parse_schedule(self, parse_info):
        result_time = self.__time_parser.parse(parse_info[1])
        result_lessons = self.__lessons_parser.parse(parse_info[2])
        result_classrooms = self.__classroom_parser.parse(parse_info[-1])
        return self.__prepare_answer(result_time, result_lessons, result_classrooms)

    def __prepare_answer(self, times, lessons, rooms):
        result_data = []
        for it in times:
            day_data = []
            temp_data = zip(times[it], lessons[it], rooms[it])
            for its in temp_data:
                day_data.append(its)
            result_data.append(day_data)
        return result_data

    def parse_header(self):
        data = 0
        it_col = START_PARSE_COL
        header_parse_list = []
        while data is not None:
            data = self.worksheet.cell(row=HEADER_ROW, column=it_col).value
            if data is not None:
                data = data.replace(' ', '')
                if data == DAY_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.Day))
                elif data == TIME_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.Time))
                elif data == CLASS_SPLIT_DATA:
                    header_parse_list.append((it_col, StructParse.NumberClass))
                else:
                    header_parse_list.append((it_col, StructParse.GroupName, data))
                it_col += 1
        return header_parse_list
