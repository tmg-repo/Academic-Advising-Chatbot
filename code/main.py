import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')

def main():
    ans = input("What can I help you with today? :)\n")
    
    help = "help"

    prereqs = "prerequisites"
    prereqs_syn = []
    for syn in wordnet.synsets(prereqs):
        for l in syn.lemmas():
            prereqs_syn.append(l.name())

    courses = "courses"
    courses_syn = []
    for syn in wordnet.synsets(courses):
        for l in syn.lemmas():
            courses_syn.append(l.name())
    
    stat = "stat"
    stat_syn = []
    for syn in wordnet.synsets(stat):
        for l in syn.lemmas():
            stat_syn.append(l.name())

    advisor = "advisor"
    advisor_syn = []
    for syn in wordnet.synsets(advisor):
        for l in syn.lemmas():
            advisor_syn.append(l.name())

    appointment = "appointment"
    app_syn = []
    for syn in wordnet.synsets(appointment):
        for l in syn.lemmas():
            app_syn.append(l.name())

    work = "work"
    work_syn = []
    for syn in wordnet.synsets(work):
        for l in syn.lemmas():
            work_syn.append(l.name())

    job = "job"
    job_syn = []
    for syn in wordnet.synsets(job):
        for l in syn.lemmas():
            job_syn.append(l.name())

    nothing = "nothing"
    nothing2 = "Nothing"
    nothing_syn = []
    for syn in wordnet.synsets(nothing):
        for l in syn.lemmas():
            nothing_syn.append(l.name())
    true = 0
    
    while true == 0:
        if courses in ans or ans in courses_syn:
            from coursesAvail import coursesAvail
            coursesAvail()
        elif work in ans or job in ans or ans in work_syn or ans in work_syn:
            from jobPossibilities import run
            run()
        elif stat in ans or ans in stat_syn:
            from coursestats import coursestats
            coursestats()
        elif advisor in ans or appointment in ans or ans in advisor_syn or ans in app_syn:
            from bookingAppointment import run
            run()
        elif prereqs in ans or ans in prereqs_syn: 
            from prereq import prereq
            prereq()
        else:
            from getHelp import get_help
            get_help()
            
        ans = input("What else can I help you with?\n")
        if nothing in ans or nothing2 in ans:
            print("Thank you for talking with me, I hope this was helpful!")
            true = 1

    

main()


