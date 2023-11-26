from .SingletonMeta import SingletonMeta
from .subject import Subject

class SubjectRepo(metaclass=SingletonMeta):
    subjects: list[Subject] = []

    def create_subject(self, name, passing_score):
        index = self.find_subject(name)
        if index != -1:
            return False
        subject = Subject(name, passing_score)
        self.subjects.append(subject)
        return True

    def get_subjects(self):
        return self.subjects
    
    def find_subject(self, name):
        try:
            return next(i for i, v in enumerate(self.subjects) if v.name == name)
        except StopIteration:
            return -1
    
    def update_subject(self, name, passing_score):
        index = self.find_subject(name)
        if index == -1:
            return False
        self.subjects[index].passing_score = passing_score
        return True

    def delete_subject(self, name):
        index = self.find_subject(name)
        if index == -1:
            return False
        self.subjects.pop(index)
        return True

    