from openpyxl.cell import Cell
from openpyxl.worksheet.worksheet import Worksheet

from document_settings import (START_PARSE_ROW,
                               END_PARSE_ROW,
                               ROWS_ON_DAY,
                               StructParse)


class LessonsParser:

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
                lesson = cell.value
                if lesson is not None:
                    result_data = lesson
            else:
                lesson_numerator = cell.value
                lesson_denominator = self.__worksheet.cell(row=it+1, column=info_parse[0]).value
                if (lesson_numerator is not None) and (lesson_denominator is not None):
                    result_data = f'{lesson_numerator} || {lesson_denominator}'
                elif (lesson_numerator is not None) and (lesson_denominator is None):
                    result_data = f'{lesson_numerator} || ---'
                elif (lesson_numerator is None) and (lesson_denominator is not None):
                    result_data = f'--- || {lesson_denominator}'
            result[current_day].append(result_data)
            count_day_rows += 1
        return result
