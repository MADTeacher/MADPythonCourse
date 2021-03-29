from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

from document_settings import (START_PARSE_ROW,
                               END_PARSE_ROW,
                               ROWS_ON_DAY,
                               StructParse)


class ClassroomParser:

    def __init__(self, worksheet: Worksheet):
        self.__worksheet = worksheet
        self.__result_parse: dict[int, list[str]] = {}

    def __check_merge(self, cell: Cell):
        for it in self.__worksheet.merged_cells.ranges:
            if cell.coordinate in it:
                return True
        return False

    def parse(self, info_parse: tuple[int, StructParse]) -> dict[int, list[str]]:
        count_day_rows = 1
        current_day = 1
        result: dict[int, list[str]] = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        }

        for it in range(START_PARSE_ROW, END_PARSE_ROW, 2):
            if count_day_rows * 2 > ROWS_ON_DAY:
                current_day += 1
                count_day_rows = 1
            result_data = "None"
            cell = self.__worksheet.cell(row=it, column=info_parse[0])
            if self.__check_merge(cell):
                room = cell.value
                if room is not None:
                    result_data = room
            else:
                room_numerator = cell.value
                room_denominator = self.__worksheet.cell(row=it+1, column=info_parse[0]).value
                if (room_numerator is not None) and (room_denominator is not None):
                    result_data = f'{room_numerator} / {room_denominator}'
                elif (room_numerator is not None) and (room_denominator is None):
                    result_data = f'{room_numerator} / -'
                elif (room_numerator is None) and (room_denominator is not None):
                    result_data = f'- / {room_denominator}'
            result[current_day].append(result_data)
            count_day_rows += 1
        return result
