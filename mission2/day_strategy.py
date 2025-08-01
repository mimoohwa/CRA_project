from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def add_points(self,player):
        ...

class MondayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(1)

class TuesdayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(1)

class WednesdayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(3)
        player.add_wed_cnt()

class ThursdayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(1)

class FridayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(1)

class SaturdayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(2)
        player.add_weekend_cnt()

class SundayStrategy(Strategy):
    def add_points(self,player):
        player.add_points(2)
        player.add_weekend_cnt()