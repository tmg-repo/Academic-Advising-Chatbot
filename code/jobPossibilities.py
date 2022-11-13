def run():
    job_Dict = {
        "COSC 301": "Data Scientist, Data Analyist",
        "COSC 303": "Quantitative Analyist, Quantitative Developer",
        "COSC 304": "Database Analyst, Database Administrator",
        "COSC 305": "Project Manager",
        "COSC 310": "Software Developer",
        "COSC 315": "Operating System Developer",
        "COSC 320": "Software Developer, Predictive Modeler, Algorithm Researcher",
        "COSC 322": "AI Developer, ML Developer",
        "COSC 328": "Network Engineer, Infastructure Engineer",
        "COSC 335": "Medical Physicist, Medical Researcher",
        "COSC 341": "UI Designer, Frontend Developer",
        "COSC 344": "Image Processing Engineer",
        "COSC 360": "Web Developer",
        "COSC 404": "Database Manager, Database Administrator",
        "COSC 407": "Parallel Computing Engineer",
        "COSC 414": "Rendering Engineer, UI Developer",
        "COSC 421": "Network Science Researcher",
        "COSC 444": "Computer Vision Engineer",
        "DATA 301": "Data Analyst",
        "DATA 310": "Regression Analyst",
        "DATA 311": "Data Scientist, Business Intelligence Developer, Machine Learnig Developer",
        "DATA 315": "Data Analyst, Data Scientist",
        "DATA 405": "Modelling/Forecasting Specialist, Stochastic Data Scientist",
        "DATA 407": "Data Analyst, Data Scientist",
        "DATA 410": "Data Scientist"
        
    }

    user_input =""

    print("Hi! Welcome to the Job Possibilities Feature. To return to the home at any time type ""exit"".")

    while user_input != "exit":
        while True:
            try:
                print("Enter a DATA or COSC course you are curretly taking:")
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
