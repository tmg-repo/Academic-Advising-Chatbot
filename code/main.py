import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

def main():
    ps = PorterStemmer()
    
    ans = input("What can I help you with today? :)\n")
    
    help = "help"
    prereqs = "prerequisites"
    courses = "courses"
    stat = "stat"
    advisor = "advisor"
    appointment = "appointment"
    work = "work"
    job = "job"
    nothing = "nothing"
    nothing2 = "Nothing"
    true = 0
    
    while true == 0:
    
        if ps.stem(courses) in ans:
            from coursesAvail import coursesAvail
            coursesAvail()
        elif ps.stem(work) in ans or ps.stem(job) in ans:
            from jobPossibilities import run
            run()
        elif ps.stem(stat) in ans:
            from coursestats import coursestats
            coursestats()
        elif ps.stem(advisor) in ans or ps.stem(appointment) in ans:
            from bookingAppointment import run
            run()
        elif ps.stem(prereqs) in ans:
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


