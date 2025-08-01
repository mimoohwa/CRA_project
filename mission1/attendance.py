import os

MAX_PLAYER = 100
TEST_SCRIPT_FILE = "attendance_weekday_500.txt"

id_cnt = 0
player_id = {}

player_points = [0] * MAX_PLAYER
player_grade = [0] * MAX_PLAYER
player_name = [''] * MAX_PLAYER
player_wed_cnt = [0] * MAX_PLAYER
player_weekend_cnt = [0] * MAX_PLAYER

def read_test_script(test_script_file):
    new_input_lines = []
    if not os.path.exists(test_script_file):
        print("파일을 찾을 수 없습니다.")
        exit()

    f = open(test_script_file, encoding='utf-8')
    for _ in range(500):
        input_line = f.readline()
        if not input_line:
            break
        if is_valid_input(input_line):
            new_input_lines.append(input_line.strip())

    return new_input_lines

def is_valid_input(input_line):
    if len(input_line.strip().split()) == 2:
        return True
    return False

def resister_player(input_lines):
    for input_line in input_lines:
        player, day = input_line.split()
        assign_player_id(player)

def assign_player_id(player):
    global id_cnt

    if player not in player_id:
        id_cnt += 1
        player_id[player] = id_cnt
        player_name[id_cnt] = player

def add_attendance_points(input_lines):
    for input_line in input_lines:
        player, day = input_line.split()
        add_attendance_points_to_player(player, day)

def add_attendance_points_to_player(player, day):
    print(player, day)
    id = player_id[player]
    add_point = 0
    if day == "monday":
        add_point += 1
    elif day == "tuesday":
        add_point += 1
    elif day == "wednesday":
        add_point += 3
        player_wed_cnt[id] += 1
    elif day == "thursday":
        add_point += 1
    elif day == "friday":
        add_point += 1
    elif day == "saturday":
        add_point += 2
        player_weekend_cnt[id] += 1
    elif day == "sunday":
        add_point += 2
        player_weekend_cnt[id] += 1

    player_points[id] += add_point

def add_bonus_points():
    for id in range(1, id_cnt + 1):
        if player_wed_cnt[id] > 9:
            player_points[id] += 10
        if player_weekend_cnt[id] > 9:
            player_points[id] += 10

def assign_grade():
    for id in range(1, id_cnt + 1):
        if player_points[id] >= 50:
            player_grade[id] = 1
        elif player_points[id] >= 30:
            player_grade[id] = 2
        else:
            player_grade[id] = 0

def print_player_score():
    for id in range(1, id_cnt + 1):
        print(f"NAME : {player_name[id]}, POINT : {player_points[id]}, GRADE : {get_player_grade(id)}")

def get_player_grade(id):
    if player_grade[id] == 1:
        return "GOLD"
    elif player_grade[id] == 2:
        return "SILVER"
    else:
        return "NORMAL"

def print_removed_player():
    print("\nRemoved player")
    print("==============")
    for id in range(1, id_cnt + 1):
        if is_removable_player(id):
            print(player_name[id])

def is_removable_player(id):
    return player_grade[id] not in (1, 2) and player_wed_cnt[id] == 0 and player_weekend_cnt[id] == 0


def main():
    input_lines = read_test_script(TEST_SCRIPT_FILE)

    resister_player(input_lines)
    add_attendance_points(input_lines)

    add_bonus_points()
    assign_grade()

    print_player_score()
    print_removed_player()


if __name__ == "__main__":
    main()
