import pytest
from attendance import AttendanceManager
import attendance_origin as sut_origin


def test_result(capsys):
    sut = AttendanceManager()
    sut.main()
    result = capsys.readouterr().out
    sut_origin.input_file()
    result_origin = capsys.readouterr().out
    assert result == result_origin