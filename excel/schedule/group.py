from schedule.daily_schedule import DailySchedule


class GroupInfo:

    def __init__(self, group_name: str):
        self.name = group_name
        self.course = group_name[0]
        self.week_schedule: dict[int, DailySchedule] = {}

    def set_week_schedule(self, day_info: DailySchedule) -> None:
        self.week_schedule[day_info.day_number] = day_info
