while True:
    import os
    import time
    Counter = 0 # defines the point where a hint or the answer can be given
    hint_iteration = 0 # tells us which hint to output
    hint_chosen = False 
    questions_answered = 0 # stats
    attempt_overall = 0 # stats
    def clear_console():
        # to clear the console for Windows
        if os.name == 'nt':
            os.system('cls')
        # to clear the console for Linux and macOS
        else:
            os.system('clear')
    def Display(): # to display stats of the player
        for i in range(7):
            if i == 0 or i == 6:
                print("+-----------------------------------+")
            elif i == 3:
                print(f"| Attempts: {attempt_overall}           Answered: {questions_answered} |")
            elif i == 3 and attempt_overall > 9:
                print(f"| {attempt_overall}                              {questions_answered} |")
            else:
                print("|                                   |")
    def Error_string_handling(): # to validate user string input
        global user_string_answer
        while True:
            try:
                user_string_answer = input()
                break
            except ValueError:
                print("Numerical values are not accepted, please make sure to enter string characters only")
            except:
                print("Unknown error detected, please make sure to enter string characters only")
    def Error_number_handling(): # to validate user number input
        global user_number_answer
        while True:
            try:
                user_number_answer = int(input())
                break
            except ValueError:
                print("Only Numerical Integer values are accepted, try again")
            except:
                print("Unknown error detected, please make sure to enter Numerical Integer values only")
    
    print("""
    ******************************************************************************
    |                      Welcome to my \"Quiz Game\" show                          |
    |                                                                              |
    |                 ----------                     ----------                    |
    |                |          |                   |          |                   |
    |                |    O    |                   |    O    |                     |
    |                |          |                   |          |                   |
    |                 ----------                     ----------                    |
    |                                                                              |
    |                           \\                         /                        |
    |                            \\                       /                         |
    |                             ---------     ---------                          |
    |                                    |       |                                 |
    |                                    |       |                                 |
    |                                     \\ _____/                                 |
    |                                                                              |
    ******************************************************************************
    """)
    print("""
    rules:
    1. Some answers require only 1 word (Case-sensitive) and others require numbers (Integers)
    2. If you fail to answer any of the questions two times, the \"hint\" option will be open for use and will keep popping around every 2 answers if you didn't choose the hint option. After 4 trials, you will be given the option to reveal the asnwer if you would like to
    3. Your stats will appear in the end of the quiz show. your "Attempts" represent the number of failed answers, while your "Answered" represents the number of questions correctly guessed
    4. Don't forget to have fun while you are at it :)
    
    """)
    quiz_questions = {
        "What is the capital of France?": "Paris",
        "How many elements are in the periodic table?": 118,
        "Which language has the most native speakers?": "Mandarin",
        "How many stars does the American flag have?": 50
    }
    for question, answer in quiz_questions.items(): #iterate through each item in the dictionary
        print(question)
        if isinstance(answer,int): # if the value is a number
            Error_number_handling()
            while user_number_answer != answer:
                attempt_overall += 1
                Counter += 1
                print("Wrong answer, try again")
                if Counter != 0 and hint_chosen == False and Counter % 2 == 0 and Counter != 4:
                    User_hint = input("Would you like a hint? press \"Y\" to proceed with the hint, otherwise press any key\n")
                    hint_chosen = True
                    if hint_iteration == 1 and (User_hint == "Y" or User_hint == "y"):
                        print("The number you are looking for is 2 less than 5 factorial!")
                    elif hint_iteration == 3 and (User_hint == "Y" or User_hint == "y"):
                        print("it is around 48 to 54")
                if Counter >= 4:
                    User_final_answer = input("Would you like to know the answer? press \"Y\" to proceed, otherwise press any key\n")
                    if User_final_answer == "Y" or User_final_answer == "y":
                        print(f"The answer was: {answer}")
                        break
                Error_number_handling()
            if user_number_answer == answer:
                print("Correct answer!")
                time.sleep(1)
                questions_answered += 1
        else: # the value is a string
            Error_string_handling()
            while user_string_answer != (answer):
                attempt_overall += 1
                Counter += 1
                print("Wrong answer, try again")
                if Counter != 0 and hint_chosen == False and Counter % 2 == 0 and Counter != 4:
                    User_hint = input("Would you like a hint? press \"Y\" to proceed with the hint, otherwise press any key\n")
                    if hint_iteration == 0 and (User_hint == "Y" or User_hint == "y"):
                        print("This place has the Eiffel Tower!")
                    elif hint_iteration == 2 and (User_hint == "Y" or User_hint == "y"):
                        print("This language is spoken by many Chinese people!")
                if Counter >= 4:
                    User_final_answer = input("Would you like to know the answer? press \"Y\" to proceed, otherwise press any key\n")
                    if User_final_answer == "Y":
                        print(f"The answer was: {answer}")
                        break
                Error_string_handling()
            if user_string_answer == answer:
                print("Correct answer!")
                time.sleep(1)
                questions_answered += 1
        hint_iteration += 1
        Counter = 0
    Display()
    Continue = input("Would you like to continue playing? please enter \"Y\". Otherwise press any key to exit\n")
    if Continue != "y" or Continue != "Y":
        break
    else:
        clear_console()
print("Thank you for playing :)")
time.sleep(2)
#if the user can't get a question correct, give him/her hints