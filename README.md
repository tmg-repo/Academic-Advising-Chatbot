# UBCO Computer Science ChatBot

Our chatBot is an acedmic tool for UBCO COSC students to aid them in the mundane tasks that come with course selection, scheduling, and acedmic advising!

The code for chatBot consists of X methods that are all ran within our main class. The main class communicates with the user and decides which class to run based on their inputs. Since each class represents one of the bot's functions, it simplifies the process considering an entire function can be enclosed in a single class. After the functions isn't needed by the user, the program takes them back to the main method and aks if any other assistance is needed. Using a while loop, the main method will run until the user has specified no more help is needed. This loop lets the user take advantage of all the functions in one coversation.


| Class | Description |
| ----------- | ----------- |
| main | Begings conversation with user, runs fuction class based on user input and continues until user no longer requires its assistance |
| getHelp | Logs user issues it found within the chatBot, storing them in csv file, and gives user pointers on how to communicate with bot.  |
| coursesAvail | Asks user what courses they've takenn and outputs the courses the user has completed the prerequisites for. |
