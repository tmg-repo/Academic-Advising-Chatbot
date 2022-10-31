import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def main():
    sent = SentimentIntensityAnalyzer()
    ans = input("What can I help you with today? :)\n")
    sent_dict = sent.polarity_scores(ans)
    max_value = max(sent_dict, key=sent_dict.get)
    
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
        if max_value == "neg":
            ans = input("I'm sorry this conversation wasn't helpful. Would you like to continue?\n")
            if "no" in ans:
                print("test")
                return
            else:
                main()
                break

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
        sent_dict = sent.polarity_scores(ans)
        max_value = max(sent_dict, key=sent_dict.get)
        if nothing in ans or nothing2 in ans:
            ans = input("How did you feel about our conversation?")
            sent_dict = sent.polarity_scores(ans)
            max_value = max(sent_dict, key=sent_dict.get)

            if max_value == "neg":
                print("I'm sorry I wasn't very useful. Thank you for the feedback!")
            elif max_value == "neu" or max_value == "compound":
                print("Thanks for the feedback!")
            elif max_value == "pos":
                print("I'm glad you had a good conversation with me!")
            true = 1
            

    

main()


