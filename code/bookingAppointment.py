def run():
    print("Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit"".")
    print("To book an academic advising appointment please follow the link provided below.")
    print("https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/")
    x = str(input())
    
    uinput(x)

def uinput(x):
    user_in = x

    if user_in == "exit":
        print("Exiting Appointment Booking")
    else:
        print("Your input is not recognised. To exit this feature please type exit")
        x = str(input())
        uinput(x)