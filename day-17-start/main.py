from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
# TODO 1)Find length of list: 12
# TODO 2)Find out how to loop through list:print(question_data[0]["text"])

for question in question_data:
    question_text= question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions:
    quiz.next_question()





