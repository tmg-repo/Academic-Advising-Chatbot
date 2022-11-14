import sys
from jobPossibilities import run
from jobPossibilities import uinput
from jobPossibilities import courseCode


def test_run_job(capsys):
    run()
    captured = capsys.readouterr()
    assert captured.out == "Hi! Welcome to the Job Possibilities Feature. To return to the home at any time type ""exit"". Otherwise hit enter\n"

def test_uinput_job(capsys):
    uinput("exit")
    captured = capsys.readouterr()
    assert captured.out == "Exiting Job Possibilities\n"

    uinput("other input")
    captured2 = capsys.readouterr()
    assert captured2.out == "Enter the three digit code associated with the COSC class you are taking:\n"

def test_course_code(capsys):
    courseCode("301")
    captured = capsys.readouterr()
    assert captured.out == "Data Scientist, Data Analyist\nThe above jobs are associated with the course you are taking\n"




