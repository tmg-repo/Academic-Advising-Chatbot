from prereq import validate
import sys

def test_validate(capsys):
    validate("COSC 101")
    captured = capsys.readouterr()
    assert captured.out == "There are no prereqs for these courses.\n"

    validate("COSC 111")
    captured = capsys.readouterr()
    assert captured.out == "There are no prereqs for these courses.\n"

    validate("COSC 421")
    captured = capsys.readouterr()
    assert captured.out == "STAT 230.\n"






