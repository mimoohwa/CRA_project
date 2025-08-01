import os
from player import Player

TEST_SCRIPT_FILE = "attendance_weekday_500.txt"

class AttendanceManager:
    def __init__(self):
        self.id_cnt = 0
        self.player_id = {}
        self.player_list = []

class TestScriptReader:
    def read_test_script(self,test_script_file: str) -> list:
        new_input_lines = []
        if not os.path.exists(test_script_file):
            print("파일을 찾을 수 없습니다.")
            exit()

        f = open(test_script_file, encoding='utf-8')
        for _ in range(500):
            input_line = f.readline()
            if not input_line:
                break
            if self.is_valid_input(input_line):
                new_input_lines.append(input_line.strip())

        return new_input_lines

    def is_valid_input(self,input_line: str) -> bool:
        if len(input_line.strip().split()) == 2:
            return True
        return False

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
        add_point = 0
        if day == "monday":
            add_point += 1
        elif day == "tuesday":
            add_point += 1
        elif day == "wednesday":
            add_point += 3
            player.add_wed_cnt()
        elif day == "thursday":
            add_point += 1
        elif day == "friday":
            add_point += 1
        elif day == "saturday":
            add_point += 2
            player.add_weekend_cnt()
        elif day == "sunday":
            add_point += 2
            player.add_weekend_cnt()

        player.add_points(add_point)


    def add_bonus_points(self) -> None:
        for player in self.player_list:
            if player.wednesday_count > 9:
                player.add_points(10)
            if player.weekend_count > 9:
                player.add_points(10)

    def assign_grade(self) -> None:
        for player in self.player_list:
            if player.points >= 50:
                player.grade = 1
            elif player.points >= 30:
                player.grade = 2
            else:
                player.grade = 0

    def print_player_score(self) -> None:
        for player in self.player_list:
            print(f"NAME : {player.name}, POINT : {player.points}, GRADE : {player.grade}")

    def get_player_grade(self,player: Player)-> str:
        if player.grade == 1:
            return "GOLD"
        elif player.grade == 2:
            return "SILVER"
        else:
            return "NORMAL"

    def print_removed_player(self) -> None:
        print("\nRemoved player")
        print("==============")
        for player in self.player_list:
            if self.is_removable_player(player):
                print(player.name)

    def is_removable_player(self,player: Player) -> bool:
        return player.grade not in (1, 2) and player.wednesday_count == 0 and player.weekend_count == 0


    def main(self):
        input_lines = self.read_test_script(TEST_SCRIPT_FILE)

        self.resister_player(input_lines)
        self.add_attendance_points(input_lines)

        self.add_bonus_points()
        self.assign_grade()

        self.print_player_score()
        self.print_removed_player()


if __name__ == "__main__":
    manager = AttendanceManager()
    manager.main()
