class Subject:
    def __init__(self, name, passing_score):
        self.name = name
        self.scores = []
        if type(passing_score) is not int:
            raise Exception('Passing score should be integer!')
        if passing_score > 100 or passing_score < 0:
            raise Exception('Passing score should be between 0 and 100 inclusive!')
        self.passing_score = passing_score

    def get_name(self):
        return self.name

    def get_passing_score(self):
        return self.passing_score

    def get_students(self):
        return [score.student for score in self.scores]
    
    def get_scores(self):
        return self.scores
    
    def __str__(self):
        return f'{self.name}, passing score: {self.passing_score}'