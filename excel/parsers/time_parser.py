from openpyxl.worksheet.worksheet import Worksheet

from document_settings import (START_PARSE_ROW,
                               END_PARSE_ROW,
                               ROWS_ON_DAY,
                               StructParse)


MyType = dict[tuple[int, StructParse], dict[int, list[str]]]


class TimeParser:

    def __init__(self, worksheet: Worksheet):
        self.__worksheet = worksheet
        self.__result_parse: dict[int, list[str]] = {}
        self.__CACHE: MyType = {}

    def parse(self, info_parse: tuple[int, StructParse]) -> dict[int, list[str]]:
        if info_parse in self.__CACHE:
            return self.__CACHE[info_parse]
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
            data = self.__worksheet.cell(row=it, column=info_parse[0]).value
            result[current_day].append(data)
            count_day_rows += 1
        self.__CACHE[info_parse] = result
        return result

