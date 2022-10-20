def coursesAvail():
    import csv
    # (assuming >=60% grades and not including co-reqs)
    # and that courses are entered in this format: COSC 301, COSC 222, DATA 301
    
    # creating courseTaken list
    courseTaken = []
    ans = input("What courses have you taken?:\n")
    courseTaken.append(ans)
    
    # accounting for third year standing prerequisite
    third = input("Are you in third year or higher? (Yes/No)\n")
    if third == "Yes" or third == "yes":
        courseTaken.append("Third Year Standing")
        courseTaken.append("")
        courseTaken.append("PREC 12")

    filename="withoutCodes.csv"
    filename2="coscCourses.csv"
    courseList = []
    courses = []
    canTake = []
    
    # opening the prerequisite file using "with" statement
    with open(filename,'r') as data:
        for line in csv.reader(data):
            courseList.append(line)
            
    # opening the course list file using "with" statement
    with open(filename2,'r') as data:
        for line in csv.reader(data):
            courses.append(line)
    
    
    # looping through courseList and verifying what sub-lists are present in courseTaken
    a = 0
    b = 0
    for list in courseList:
        a = 0
        for item in list:
            if item in courseTaken:
                a +=1
        
        if a == len(list):
              canTake.append(courses[b])
              
        b +=1
    
    # removing duplicate variables
    canTake2 = []
    [canTake2.append(x) for x in canTake if x not in canTake2]   
    
    # removing courses already taken
    canTakeFinal = [x for x in canTake2 if x not in courseTaken]      
                            
    # make string without brackets in list and return string
    courseString = ", ".join(repr(e) for e in canTakeFinal)
    prMes = f"The courses you're qualified to take are: {courseString}"
    print(prMes) 
    

