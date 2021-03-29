import openpyxl
import json

from schedule_builder import ScheduleBuilder

if __name__ == '__main__':
    wb = openpyxl.load_workbook("red_raspisanie_o_iita_2.xlsx")
    sheet = wb.active
    builder = ScheduleBuilder(sheet)
    data = builder.build()
    json.dump(data, fp=open('my_schedule.json', 'w', encoding='utf-8'), indent=4)
    info = json.load(open('my_schedule.json'))
    my_schedule = info['1-МДА-9'][str(1)]
    print(my_schedule)

