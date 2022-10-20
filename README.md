# UBCO Computer Science ChatBot

Our chatBot is an academic tool for UBCO COSC students to aid them in the mundane tasks that come with course selection, scheduling, and acedmic advising!

The code for chatBot consists of 8 classes that are all run within our main class. The main class communicates with the user and decides which class to run based on their inputs. Since each class represents one of the bot's functions, it simplifies the process considering an entire function can be enclosed in a single class. After the functions isn't needed by the user, the program takes them back to the main method and aks if any other assistance is needed. Using a while loop, the main method will run until the user has specified no more help is needed. This loop lets the user take advantage of all the functions in one conversation.


| Class | Description |
| ----------- | ----------- |
| main | Begins conversation with user, runs fuction class based on user input and continues until user no longer requires its assistance |
| getHelp | Logs user issues it found within the chatBot, storing them in a csv file, and gives user pointers on how to communicate with the bot.  |
| coursesAvail | Asks user what courses they've taken and outputs the courses the user has completed the prerequisites for. |
| prereq | Prompts user to enter a COSC course that they would like to know the prerequisities for, and validates their input to ensure it is correct |
| jobPossibilities | Asks user what course COSC course they are taking and returns potential jobs associated with that course |
| bookingAppointment | Allows users to book academic advising appointments by providing the URL to the UBCO academic advising website | 
