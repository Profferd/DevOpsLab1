from .SingletonMeta import SingletonMeta
from .student import Student

class StudentRepo(metaclass=SingletonMeta):
    students: list[Student] = []

    def create_student(self, first_name, last_name):
        index = self.find_student(first_name, last_name)
        if index != -1:
            return False
        student = Student(first_name, last_name)
        self.students.append(student)
        return True
    
    def get_students(self):
        return self.students
    
    def find_student(self, first_name, last_name):
        try:
            return next(i for i, student in enumerate(self.students) if student.first_name == first_name and student.last_name == last_name)
        except StopIteration:
            return -1

    def delete_student(self, first_name, last_name):
        index = self.find_student(first_name, last_name)
        if index == -1:
            return False
        self.students.pop(index)
        return True