class Subject:
    def __init__(self, name, passing_score):
        self.name = name
        self.scores = []
        self.passing_score = passing_score

    def get_name(self):
        return self.name

    def get_passing_score(self):
        return self.passing_score

    def get_students(self):
        return [score.student for score in self.scores]

