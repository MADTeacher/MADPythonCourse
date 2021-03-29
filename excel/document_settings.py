from enum import IntEnum

DAY_SPLIT_DATA = "Днинед."
TIME_SPLIT_DATA = "Часы"
CLASS_SPLIT_DATA = "№ауд."

HEADER_ROW = 3
START_PARSE_ROW = 4
START_PARSE_COL = 1
ROWS_ON_DAY = 10
END_PARSE_ROW = START_PARSE_ROW + 6 * ROWS_ON_DAY
DAY_OFF_COUNT = 5

class StructParse(IntEnum):
    Day = 1
    Time = 2
    GroupName = 3
    NumberClass = 4
