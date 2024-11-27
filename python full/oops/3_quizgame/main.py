from questionmodel import Question #class
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_ques=Question(question_text,question_answer)
    question_bank.append(new_ques)
# print(question_bank)

quiz=QuizBrain(question_bank)
for i in range(0,len(question_bank)):
    quiz.next_question_ans_score()    
    print("-----------------------------")
