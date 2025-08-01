class Player:
    def __init__(self, name):
        self._name = name
        self._points = 0
        self._grade = 0
        self._wednesday_cnt = 0
        self._weekend_cnt = 0

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    def add_points(self, value: int):
        self._points += value

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value: int):
        self._grade = value

    @property
    def wednesday_count(self):
        return self._wednesday_cnt

    def add_wed_cnt(self):
        self._wednesday_cnt += 1

    @property
    def weekend_count(self):
        return self._weekend_cnt

    def add_weekend_cnt(self):
        self._weekend_cnt += 1



