from day_strategy import *

class StrategyFactory:
    def get_strategy(self, day):
        if day == "monday":
            return MondayStrategy()
        elif day == "tuesday":
            return TuesdayStrategy()
        elif day == "wednesday":
            return WednesdayStrategy()
        elif day == "thursday":
            return ThursdayStrategy()
        elif day == "friday":
            return FridayStrategy()
        elif day == "saturday":
            return SaturdayStrategy()
        elif day == "sunday":
            return SundayStrategy()
        else:
            return
