def run():
    print("Hi! Welcome to the Job Possibilities Feature. To return to the home at any time type ""exit"". Otherwise hit enter")

    x = str(input())
    
    uinput(x)

def uinput(x):
    user_in = x

    if user_in == "exit":
        print("Exiting Job Possibilities")
    else:
        print("Enter the three digit code associated with the COSC class you are taking:")
        # y = str(input())
        # courseCode(y)


def courseCode(x):
    job_Dict = {
        "301": "Data Scientist, Data Analyist",
        "303": "Quantitative Analyist, Quantitative Developer",
        "304": "Database Analyst, Database Administrator",
        "305": "Project Manager",
        "310": "Software Developer",
        "315": "Operating System Developer",
        "320": "Software Developer, Predictive Modeler, Algorithm Researcher",
        "322": "AI Developer, ML Developer",
        "328": "Network Engineer, Infastructure Engineer",
        "335": "Medical Physicist, Medical Researcher",
        "341": "UI Designer, Frontend Developer",
        "344": "Image Processing Engineer",
        "360": "Web Developer",
        "404": "Database Manager, Database Administrator",
        "407": "Parallel Computing Engineer",
        "414": "Rendering Engineer, UI Developer",
        "421": "Network Science Researcher",
        "444": "Computer Vision Engineer"
    }

    try:
        print(job_Dict[x])
        print("The above jobs are associated with the course you are taking")
    except NameError:
                print("The course code you have entered is not recognised. Please try again or exit.")
    except KeyError:
                print("The course code you have entered is not recognised. Please try again or exit.")
    
    # print("Press the enter key if you wish to search for another course. If not type exit.")
    # user_second = str(input())

    # if user_second != "exit":
    #     print("Enter the three digit code associated with the COSC class you are taking:")
    #     uinput(user_second)

   
