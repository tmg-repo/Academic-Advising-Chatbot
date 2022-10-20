def prereq():  
        courses = ["COSC 101", "COSC 111", "COSC 121", "COSC 122", "COSC 123", "COSC 210", "COSC 211", "COSC 221", "COSC 222", "COSC 301", "COSC 303", "COSC 304", "COSC 305", "COSC 310", "COSC 315", "COSC 320", "COSC 322", "COSC 328", "COSC 335", "COSC 341", "COSC 344", "COSC 360", "COSC 404", "COSC 407", "COSC 414", "COSC 421", "COSC 444", "COSC 499"]

        def user_input():
            inp = input("What COSC course would you like a prereq for? (enter in format COSC xxx)\n")
            return inp

        def validate(str):
            if  str in courses:
                if(str=="COSC 101" or str=="COSC 111" or str=="COSC 122"):
                    print("There are no prereqs for these courses.")
                elif(str=="COSC 121"):
                    print("A score of 60 percent or higher in one of COSC 111, COSC 123.")
                elif(str=="COSC 123"):
                    print("One of COSC 111, COSC 122.")
                elif(str=="COSC 210"):
                    print("One of APSC 177, COSC 111.")
                elif(str=="COSC 211"):
                    print(" COSC 121.")
                elif(str=="COSC 221"):
                    print("One of MATH 101, MATH 142, APSC 173.")
                elif(str=="COSC 222"):
                    print(" A score of 60 percent or higher in COSC 121.")
                elif(str=="COSC 301"):
                    print("(Either (a) third-year standing, or (b) one of COSC 111 or COSC 122).")
                elif(str=="COSC 303"):
                    print("All of MATH 200, MATH 221 and either (a) COSC 111 or (b) DATA 301.")
                elif(str=="COSC 304"):
                    print("One of COSC 111, COSC 123, COSC 210. (Third-year standing.)")
                elif(str=="COSC 305"):
                    print("There are no prereqs, but COSC 310 is a coreq.")
                elif(str=="COSC 310"):
                    print("One of COSC 210, COSC 222, COSC 223. (and third-year standing.)")
                elif(str=="COSC 315"):
                    print("All of COSC 221, COSC 222.")
                elif(str=="COSC 320"):
                    print("All of COSC 221, COSC 222 and one of MATH 221, APSC 179.")
                elif(str=="COSC 322"):
                    print("All of COSC 221, COSC 222.")
                elif(str=="COSC 328"):
                    print("All of COSC 211, COSC 222.")
                elif(str=="COSC 335"):
                    print("A score more than 60 percent in COSC 222 and a score more than 60 percent in one of PHYS 102, PHYS 121, PHYS 122. (PHYS 102 or PHYS 121 preferred.)")
                elif(str=="COSC 341"):
                    print("One of COSC 111, COSC 121, COSC 123, DATA 301. (and Third-year standing.)")
                elif(str=="COSC 344"):
                    print("One of COSC 210, COSC 222 and one of MATH 200, APSC 248 and one of MATH 221, APSC 179.")
                elif(str=="COSC 360"):
                    print("All of COSC 121, COSC 304. (and third-year standing.)")
                elif(str=="COSC 404"):
                    print("COSC 304. (and third-year standing.)")
                elif(str=="COSC 407"):
                    print("Either (a) COSC 111 or (b) APSC 177. (Third-year standing is required.)")
                elif(str=="COSC 414"):
                    print("All of COSC 221, COSC 222 and one of MATH 221, APSC 179.")
                elif(str=="COSC 421"):
                    print("STAT 230.")
                elif(str=="COSC 444"):
                    print("COSC 344.")
                elif(str=="COSC 499"):
                    print("All of COSC 304, COSC 310, COSC 341.")
            
        inp = user_input()

        while((inp in courses)==False):
            print("Please enter in correct format \n")
            inp = user_input()

        validate(inp)


