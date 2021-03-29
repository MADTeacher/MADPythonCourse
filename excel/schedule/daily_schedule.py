

class DailySchedule:
    def __init__(self, day_number: int, day_off: bool = False):
        self.day_number = day_number
        self.day_off = day_off
        self.lessons: list[tuple[str, str, str]] = []