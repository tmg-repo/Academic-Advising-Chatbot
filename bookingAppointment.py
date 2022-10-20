def start():
    print("Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit"".")
    return

def exit():
    print("Exiting Appointment Booking")
    return
        
def appointment():
    print("To book an academic advising appointment please follow the link provided below.")
    print("https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/")
    return

def error():
    print("Your input is not recognised. To exit this feature please type exit")
    return

user_input = ""

start()
appointment()
while user_input != "exit":
    user_input = str(input())
    if user_input == "exit":
        exit()
    else: 
        error()