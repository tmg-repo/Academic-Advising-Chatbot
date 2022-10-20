
def get_help():
    import csv
    
    issues = []
    filename = "issues.csv"
    rows = []
    true = 0
    
    # while loop that lopps until user is satisfied with conversation
    while true == 0:
        val = input("What can I help you with?\nI'd like some pointers\nor\nReport an issue\n")
    
        # if statement to branch off according to issue
        if val == "Report an issue" or val == "report an issue":
            iss = input("Which category would your issue fit in?\nNo Response\nMisinterpretation\nOther\n")
            if iss == "No response" or iss == "No Response" or iss == "no response":
                des = input("Please decribe the issue:\n")
                rows.append(["No Response", des])
                sat = input("Thank you for logging your issue. Do you need more help? (Yes/No)\n")
                if sat == "no" or sat == "No":
                    true = 1
        
            elif iss == "Misinterpretation" or iss == "misinterpretation":
                des = input("Please decribe the issue:\n")
                rows.append(["Misinterpretation", des])
                sat = input("Thank you for logging your issue. Do you need more help? (Yes/No)\n")
                if sat == "no" or sat == "No":
                    true = 1
                
            elif iss == "Other" or iss == "other":
                des = input("Please decribe the issue:\n")
                rows.append(["Other", des])
                sat = input("Thank you for logging your issue. Do you need more help? (Yes/No)\n")
                if sat != "yes" or sat != "Yes":
                    true = 1
                
            else:
                print("Return and enter a valid input")
    
            # giving tips on how to use chatbot  
        elif val == "I'd like some pointers" or val == "i'd like some pointers" or val == "id like some pointers":
            print("My abilities can be reduced to five features that I hope you take advantage of!\nIf you want to know a class' prerequisites, ask me something like this, 'How can I take COSC 301'.\nYou can get statistics on a computer science course by asking a question about a specific course.\nPossible job oppourtunites based on your course experice can be provided if you ask about work.\nI can help you make an acedmic advising appointment aswell, just ask me how!\nIf you're unnsure what courses your experience qualifies you for, I can provide you with a list of courses you've completed the prerequisites for if you ask for help with course scheduling.\nI hope you found this helpful!!")
            
            sat = input("Do you need more help? (Yes/No)\n")
            if sat != "yes" or sat != "Yes":
                print("returning you to main...")
                true = 1
            
        else:
            print("Return and enter a valid input")
            
    
    # writing issues to issues.csv
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)    
        csvwriter.writerows(rows)
        
    
