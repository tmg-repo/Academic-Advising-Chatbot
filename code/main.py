import spacy
from spacy import displacy

def main():
    NER = spacy.load("en_core_web_sm")
    print("Hi I'm an academic advising chatbot!")
    ans = input("Before we get started tell me a bit about yourself:\n")
    ans = NER(ans)
    name = ""
    for word in ans.ents:
        if "PERSON" in word.label_:
            name = word.text
    if name != "":
        print(f"Hello {name}! It's great to meet you!")
    else:
        print("Hi! It's great to meet you!")

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
    
        if courses in ans:
            from coursesAvail import coursesAvail
            coursesAvail()
        elif work in ans or job in ans:
            from jobPossibilities import run
            run()
        elif stat in ans:
            from coursestats import coursestats
            coursestats()
        elif advisor in ans or appointment in ans:
            from bookingAppointment import run
            run()
        elif prereqs in ans:
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


