from strategy_factory import StrategyFactory
from script_reader import ScriptReader
from grade_manager import GradeManager
from bonus_strategy import BonusStrategy
from player import Player

TEST_SCRIPT_FILE = "attendance_weekday_500.txt"

class AttendanceManager:
    def __init__(self):
        self.id_cnt = 0
        self.player_id = {}
        self.player_list = []

    def resister_player(self,input_lines: list) -> None:
        for input_line in input_lines:
            player, day = input_line.split()
            self.assign_player_id(player)

    def assign_player_id(self, player_name: str) -> None:
        if player_name not in self.player_id:
            self.player_id[player_name] = self.id_cnt
            self.player_list.append(Player(player_name))
            self.id_cnt += 1

    def add_attendance_points(self,input_lines: list) -> None:
        for input_line in input_lines:
            player, day = input_line.split()
            self.add_attendance_points_to_player(player, day)

    def add_attendance_points_to_player(self, player_name: str, day: str) -> None:
        player = self.player_list[self.player_id[player_name]]

        strategy_factory = StrategyFactory()
        strategy = strategy_factory.get_strategy(day)
        strategy.add_points(player)

    def assign_grade(self) -> None:
        for player in self.player_list:
            grade_manager = GradeManager()
            player.grade = grade_manager.get_grade(player)

    def add_bonus_points(self) -> None:
        for player in self.player_list:
            bonus_strategy = BonusStrategy()
            bonus_strategy.add_points(player)

    def print_player_score(self) -> None:
        for player in self.player_list:
            print(f"NAME : {player.name}, POINT : {player.points}, GRADE : {player.grade}")

    def print_removed_player(self) -> None:
        print("\nRemoved player")
        print("==============")
        for player in self.player_list:
            if self.is_removable_player(player):
                print(player.name)

    def is_removable_player(self,player: Player) -> bool:
        return player.grade not in (1, 2) and player.wednesday_count == 0 and player.weekend_count == 0


    def main(self):
        reader = ScriptReader()
        input_lines = reader.read_test_script(TEST_SCRIPT_FILE)

        self.resister_player(input_lines)
        self.add_attendance_points(input_lines)

        self.add_bonus_points()
        self.assign_grade()

        self.print_player_score()
        self.print_removed_player()

