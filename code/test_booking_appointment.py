from bookingAppointment import run
from bookingAppointment import uinput
import sys

# def test():
#     assert run() == "Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit""." + "To book an academic advising appointment please follow the link provided below." + "https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/"

def test_uinput(capfd):
    x = uinput("exit")
    x,err=capfd.readouterr()
    assert x == "Exiting Appointment Booking"
    
    