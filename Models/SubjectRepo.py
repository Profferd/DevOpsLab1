from SingletonMeta import SingletonMeta
from subject import Subject

class SubjectRepo(metaclass=SingletonMeta):
    subjects = []

    def create_subject(self, name, passing_score):
        filtered_elements = list(filter(lambda subject: subject.name == name, self.subjects))
        if filtered_elements:
            return False
        subject = Subject(name, passing_score)
        self.subjects.append(subject)
        return True

    def get_subjects(self):
        return self.subjects
    
    def update_subject(self, name, passing_score):
        try:
            index = next(i for i, v in enumerate(self.subjects) if v.name == name)
        except StopIteration:
            return False
        self.subjects[index].passing_score = passing_score
        return True

    def delete_subject(self, name):
        try:
            index = next(i for i, v in enumerate(self.subjects) if v.name == name)
        except StopIteration:
            return False
        self.subjects.pop(index)
        return True

    