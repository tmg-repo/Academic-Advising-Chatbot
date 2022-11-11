from bookingAppointment import run
from bookingAppointment import uinput
import sys

def test_run(capsys):
    #make sure to comment out inner function to isolate the unit test
    
    run()
    captured = capsys.readouterr()
    assert captured.out == "Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit"".\n" + "To book an academic advising appointment please follow the link provided below.\n" + "https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/\n"

def test_uinput(capsys):
    #make sure to comment out inner function to isolate the unit test
    
    uinput("exit")
    captured = capsys.readouterr()
    assert captured.out == "Exiting Appointment Booking\n"

    uinput("fhfhfhf")
    captured2 = capsys.readouterr()
    assert captured2.out == "Your input is not recognised. To exit this feature please type exit\n"

    
    