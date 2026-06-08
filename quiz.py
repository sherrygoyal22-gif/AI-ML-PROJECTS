print("Welcome to AI Quiz")


subject = input("Choose Subject (Python/Statistics/Maths): ")

score = 0
python_questions = ["Q1:What is keyword used for loops in python?", 
             "Q2:Which function is used to take input from the user?",
             "Q3:Which function is used to display output on the screen?",
             "Q4:Which data type is used to store multiple values in Python?",
             "Q5:Which keyword is used to make a decision in Python?"]

python_answers = ["for", "input", "print", "list", "if"]

statistics_questions = [
    "What is the average called in statistics?",
    "Which measure shows spread of data?",
    "What is the middle value called?",
    "What is the most frequent value called?",
    "What is the symbol of mean?"
]

statistics_answers = [
    "mean",
    "standard deviation",
    "median",
    "mode",
    "x bar"
]

maths_questions = [
    "What is 5 + 5?",
    "What is 10 x 2?",
    "What is the square of 4?",
    "What is 20 / 4?",
    "What is 15 - 5?"
]

maths_answers = [
    "10",
    "20",
    "16",
    "5",
    "10"
]
if subject.lower() == "python":
    questions = python_questions
    answers = python_answers

elif subject.lower() == "statistics":
    questions = statistics_questions
    answers = statistics_answers

elif subject.lower() == "maths":
    questions = maths_questions
    answers = maths_answers

else:
    print("Invalid Subject")
    exit()

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")

    if user_answer.lower() == answers[i].lower():
        print("correct!")
        score = score + 1
    else:
        print("wrong!")
        print("correct answer:", answers[i])
print("Quiz finished")
print("Your score:", score,"/", len(questions))
if score == len(questions):
    print("Excellent!")

elif score >= 3:
    print("Good Job!")

else:
    print("Keep Practicing!")


score = 0
answer = input("What is keyword used for loops in python?")
if answer == "for":
    print("correct!")
    score = score + 1
elif answer == "while":
    print("correct")
    score = score + 1
else:
    print("wrong!")


answer2 = input("Which function is used to take input from the user?")
if answer2 == "input":
    print("correct!")
    score = score + 1
else:
    print("wrong!")

print("Your score:", score)

answer2 = input("Which function is used to take input from the user?")
if answer2 == "input":
    print("correct!")
    score = score + 1
else:
    print("wrong!")


answer3 = input("Which function is used to display output on the screen?")
if answer3 == "print":
    print("correct!")
    score = score + 1
else:
    print("wrong!")

print("Your score:", score)

answer4 = input("Which data type is used to store multiple values in Python?")
if answer4 == "list":
    print("correct!")
    score = score + 1
else:
    print("wrong!")

print("Your score:", score)

answer5 = input("Which keyword is used to make a decision in Python?")
if answer5 == "if":
    print("correct!")
    score = score + 1
else:
    print("wrong!")

print("Your score:", score)

