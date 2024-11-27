class QuizBrain:

    def __init__(self,question_list):
        self.quesno=0
        self.question_list=question_list
        self.score=0

    def next_question_ans_score(self):
        ans=input(f"Q.{self.quesno+1}:{(self.question_list[self.quesno].text)}(t/f ?)")
        if ans==self.question_list[self.quesno].answer:
            print("You are Correct ! ")
            print(f"the ans was : {self.question_list[self.quesno].answer}")
            print(f"Your score is : {self.score+1}/{self.quesno+1}")
            self.score+=1
        else:
            print("Better luck next time ! ")
            print(f"the ans was : {self.question_list[self.quesno].answer}")
            print(f"Your score is : {self.score}/{self.quesno+1}")
            # self.score+=1
        self.quesno+=1
        
