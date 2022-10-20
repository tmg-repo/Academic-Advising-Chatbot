def run():
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

    user_input =""

    print("Hi! Welcome to the Job Possibilities Feature. To return to the home at any time type ""exit"".")

    while user_input != "exit":
        while True:
            try:
                print("Enter the three digit code associated with the COSC class you are taking:")
                user_input = str(input())
                if user_input == "exit":
                    print("Exiting Job Possibilities")
                    return
                else:
                    print(job_Dict[user_input])
                    print("The above jobs are associated with the course you are taking")
                break
            except NameError:
                print("The course code you have entered is not recognised. Please try again or exit.")
            except KeyError:
                print("The course code you have entered is not recognised. Please try again or exit.")

    print("Press the enter key if you wish to search for another course. If not type exit.")
    user_input = str(input())
