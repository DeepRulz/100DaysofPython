class QuizBrain:
    def __init__(self, questions):
        self.qno = 0
        self.bank = questions
        self.score = 0

    def stillquestions(self):
        return not (self.qno >= len(self.bank))

    def next_question(self):
        cqm = self.bank[self.qno]
        cq = cqm.text
        a = input(f"Q.{self.qno + 1}: {cq} (True/False)?: ")
        self.checkanswer(a, cqm.answer)
        self.qno += 1

    def checkanswer(self, ua, ca):
        if ua.lower() == ca.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was:{ca}")
        print(f"Your current score is: {self.score}/{self.qno + 1}")
