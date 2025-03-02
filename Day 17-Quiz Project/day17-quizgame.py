from day17question_model import Question
from day17data import question_data
from day17quiz_brain import QuizBrain

k = 0
question_bank = []
for i in question_data:
    q = i["text"]
    a = i["answer"]
    question_bank.append(Question(q, a))
quiz = QuizBrain(question_bank)
while quiz.stillquestions():
    quiz.next_question()
