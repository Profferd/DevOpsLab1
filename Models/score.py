class Score:
    def __init__(self, student, subject, score):
        if type(score) is not int:
            raise Exception('Score should be integer!')
        if score > 100 or score < 0:
            raise Exception('Score should be between 0 and 100 inclusive!')
        self.student = student
        self.subject = subject
        self.score = score

    def __str__(self):
        return f'Student {self.student} received a {self.score} in {self.subject}.'
    
