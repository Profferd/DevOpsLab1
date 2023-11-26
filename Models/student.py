class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.scores = []

    def gpa(self):
        if len(self.scores) == 0:
            return 0.0
        return sum([score.score for score in self.scores]) / len(self.scores)
    
    def get_scores(self):
        return self.scores
    
    def subjects(self):
        return [score.subject for score in self.scores]
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def passed_subjects(self):
        return [score.subject for score in self.scores if score.score >= score.subject.get_passing_score()]
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, GPA: {self.gpa()}.'
    
