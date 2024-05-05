import pandas as pd
import random
import time

# Function to select specific number of questions from each difficulty level
def select_questions(file_path, sheet_name, num_questions):
    # Read all questions from the specified sheet
    all_questions = pd.read_excel(file_path, sheet_name)
    
    # Shuffle the questions
    shuffled_questions = all_questions.sample(frac=1).reset_index(drop=True)
    
    # Select the desired number of questions
    selected_questions = shuffled_questions.iloc[:num_questions]
    
    return selected_questions
#subject choice for user
def sub():
    print("Choose the subject for quiz")
    print("1. PYTHON\n2. FDS\n3. C Language")
    subject = int(input("Enter your choice: "))
    while(subject is not (1 or 2 or 3)):
        print("Invalid choice. ")
        subject= int(input("Please enter again(1/2/3): "))
    total_marks = int(input("Enter total marks for the question paper (50/100): "))
    
    while(total_marks is not (50 or 100)):
        print("Invalid choice. ")
        total_marks = int(input("Enter total marks for the question paper (50/100): "))
    
    easy_num=0
    medium_num=0
    hard_num=0
    
    if total_marks==50:
        easy_num=5
        medium_num=15
        hard_num=5
    else:
        easy_num=10
        medium_num=30
        hard_num=10
    
    easy_marks=1*easy_num
    medium_marks=2*medium_num
    hard_marks=3*hard_num
    
    if subject == 1:
        easy = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "PYTHON-EASY", easy_num)
        medium = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "PYTHON-MEDIUM", medium_num)
        hard = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "PYTHON-HARD", hard_num)
    elif subject == 2:
        easy = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "FDS-EASY", easy_num)
        medium = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "FDS-MEDIUM", medium_num)
        hard = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "FDS-HARD", hard_num)
    elif subject == 3:
        easy = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "C-EASY", easy_num)
        medium = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "C-MEDIUM", medium_num)
        hard = select_questions("C:\\Users\\Sai\\Documents\\VS Code\\QUIZ\\QuizDatabase.xlsx", "C-HARD", hard_num)
    else:
        print("Invalid choice. Please enter a valid level.")
        return None
    total_marks=easy_marks+medium_marks+hard_marks
    
    return easy, easy_marks, medium, medium_marks, hard, hard_marks, total_marks

def quiz():
    while True:  # Run the quiz until the user chooses not to repeat
        easy_questions, easy_marks, medium_questions, medium_marks, hard_questions, hard_marks, total_marks = sub()
        if easy_questions is not None and medium_questions is not None and hard_questions is not None:
            questions = pd.concat([easy_questions, medium_questions, hard_questions])

            easy_questions = easy_questions.sample(frac=1).reset_index(drop=True)
            medium_questions = medium_questions.sample(frac=1).reset_index(drop=True)
            hard_questions = hard_questions.sample(frac=1).reset_index(drop=True)

            shuffled_questions = pd.concat([easy_questions, medium_questions, hard_questions])

            correct = 0
            incorrect = 0
            marks = 0
            cl = ['Sr.No.', 'Question', 'A', 'B', 'C', 'D']
            #Display easy level questions
            print()
            print("EASY LEVEL QUESTIONS")
            print(f"Each question carries 1 mark.")
            for index, row in easy_questions.iterrows():
                print()
                print(index+1, row[cl[1]])
                print("\tA. ", row[cl[2]])
                print("\tB. ", row[cl[3]])
                print("\tC. ", row[cl[4]])
                print("\tD. ", row[cl[5]])

                user_answer = input("Enter your answer: ").capitalize()
                if user_answer not in ('A', 'B', 'C', 'D'):
                    print("Invalid Choice")
                elif user_answer == row['Answer']:
                    correct += 1
                    marks += 1
                else:
                    incorrect += 1

            #Display medium level questions
            print()
            print("MEDIUM LEVEL QUESTIONS")
            print(f"Each question carries 2 marks.")

            for index, row in medium_questions.iterrows():
                print()
                print(index+1, row[cl[1]])
                print("\tA. ", row[cl[2]])
                print("\tB. ", row[cl[3]])
                print("\tC. ", row[cl[4]])
                print("\tD. ", row[cl[5]])

                user_answer = input("Enter your answer: ").capitalize()
                if user_answer not in ('A', 'B', 'C', 'D'):
                    print("Invalid Choice")
                elif user_answer == row['Answer']:
                    correct += 1
                    marks += 2
                else:
                    incorrect += 1

            #Display hard level questions
            print()
            print("HARD LEVEL QUESTIONS")
            print(f"Each question carries 3 marks.")
            
            for index, row in hard_questions.iterrows():
                print()
                print(index+1, row[cl[1]])
                print("\tA. ", row[cl[2]])
                print("\tB. ", row[cl[3]])
                print("\tC. ", row[cl[4]])
                print("\tD. ", row[cl[5]])
                
                user_answer = input("Enter your answer: ").capitalize()
                if user_answer not in ('A', 'B', 'C', 'D'):
                    print("Invalid Choice")
                elif user_answer == row['Answer']:
                    correct += 1
                    marks += 3
                else:
                    incorrect += 1

            percent_score = (marks / total_marks) * 100

            print()
            print(f"Out of {len(shuffled_questions)} questions:")
            print(f"Correctly answered questions: {correct}")
            print(f"Incorrectly answered questions: {incorrect}")
            print(f"Your Score is: {marks} out of {total_marks} ({percent_score:.2f}%)")

            if percent_score < 35:
                print("You scored less than 35%.\nYou need to review the topics and try again.")
            elif percent_score > 80:
                print("Congratulations! You scored above 80%. Well done!")
            else:
                print("You did well. Keep practicing to improve your score!")
            print()
            ans_key=int(input("Do you want to see the answer key(1/0): "))
            if(ans_key==1):                
                print("ANSWER KEY\n")
                print("EASY LEVEL\n")
                for index, row in easy_questions.iterrows():
                    print()
                    print(index+1, row[cl[1]],"\n","Answer:- ",row["Answer"])
                print("\nMEDIUM LEVEL\n")
                for index, row in medium_questions.iterrows():
                   print()
                   print(index+1, row[cl[1]],"\n","Answer:- ",row["Answer"])  
                print("\nHARD LEVEL\n")
                for index, row in hard_questions.iterrows():
                   print()
                   print(index+1, row[cl[1]],"\n","Answer:- ",row["Answer"])

        repeat = int(input("Do you want to repeat the quiz? (1/0): "))
        if repeat != 1:
            break
        
print('\nWelcome to the ONLINE QUIZ PLATFORM😊\n')
username = input ('Enter your name: ')
print(f'Welcome {username}\n')
while True: 
    choice = int(input('Are you ready to start the quiz(1/0): '))
    if choice !=1:
        print('Thank you for using online quiz platform 😊')
        break
    else:
        quiz()
