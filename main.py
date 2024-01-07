from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# import random

question_bank = []

for i in range(len(question_data)):
    question = question_data[i]["question"]
    answer = question_data[i]["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
