import pytest
from attendance import AttendanceManager
import attendance_origin as sut_origin
from script_reader import ScriptReader

TEST_SCRIPT_FILE = "attendance_weekday_500.txt"
TEST_SCRIPT_FILE_ERR1 = "attendance_weekday_500_err1.txt"


def test_result(capsys):
    sut = AttendanceManager()
    sut.main()
    result = capsys.readouterr().out
    sut_origin.input_file()
    result_origin = capsys.readouterr().out
    assert result == result_origin

def test_no_input_file(capsys):
    sut = ScriptReader()
    sut.read_test_script(TEST_SCRIPT_FILE_ERR1)
    result = capsys.readouterr().out
    assert result == "파일을 찾을 수 없습니다.\n"