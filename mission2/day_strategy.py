from abc import ABC, abstractmethod

class Strategy(ABC):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def add_points(self):
        ...

class MondayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(1)

class TuesdayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(1)

class WednesdayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(3)
        self.player.add_wed_cnt()

class ThursdayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(1)

class FridayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(1)

class SaturdayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(2)
        self.player.add_weekend_cnt()

class SundayStrategy(Strategy):
    def add_points(self):
        self.player.add_points(2)
        self.player.add_weekend_cnt()