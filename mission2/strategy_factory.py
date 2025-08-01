from day_strategy import *

class StrategyFactory:
    def get_strategy(self, player, day):
        if day == "monday":
            return MondayStrategy(player)
        elif day == "tuesday":
            return TuesdayStrategy(player)
        elif day == "wednesday":
            return WednesdayStrategy(player)
        elif day == "thursday":
            return ThursdayStrategy(player)
        elif day == "friday":
            return FridayStrategy(player)
        elif day == "saturday":
            return SaturdayStrategy(player)
        elif day == "sunday":
            return SundayStrategy(player)
        else:
            return
