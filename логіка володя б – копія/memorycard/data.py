class Question():
    def __init__(self, name ,correct, wrong1, wrong2, wrong3):
        self.name = name
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def check(self,mny_variant):
        if mny_variant == self.correct:
            return True
        else:
            return False
