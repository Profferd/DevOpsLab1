from SingletonMeta import SingletonMeta
from student import Student

class StudentRepo(metaclass=SingletonMeta):
    students = []

    def create_student(self, first_name, last_name):
        filtered_elements = list(filter(lambda student: student.first_name == first_name and student.last_name == last_name, self.students))
        if filtered_elements:
            return False
        student = Student(first_name, last_name)
        self.students.append(student)
        return True
    
    def get_students(self):
        return self.students
    
    def delete_student(self, first_name, last_name):
        try:
            index = next(i for i, student in enumerate(self.students) if student.first_name == first_name and student.last_name == last_name)
        except StopIteration:
            return False
        self.students.pop(index)
        return True