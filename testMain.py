import unittest

from Models.StudentRepo import StudentRepo
from Models.SubjectRepo import SubjectRepo
from Models.score import Score

students = StudentRepo()
subjects = SubjectRepo()
class MyTestCase(unittest.TestCase):
    def test_correct_information(self):

        students.create_student('Dmytro', 'Hrushko')
        subjects.create_subject('DevOps', 60)
        student = students.get_students()[0]
        subject = subjects.get_subjects()[0]
        score = Score(student, subject, 98)
        student.get_scores().append(score)
        subject.get_scores().append(score)
        self.assertEqual('\n'.join(map(str, students.get_students())) or 'None', 'Dmytro Hrushko, GPA: 98.0.')
        subjects.delete_subject("DevOps")

    def test_incorrect_subject_information(self):
        subjects1 = SubjectRepo()
        with self.assertRaises(Exception):
            subjects1.create_subject('DevOps', 'sixty')

    def test_none_students(self):
        students.delete_student("Dmytro", "Hrushko")
        self.assertEqual('\n'.join(map(str, students.get_students())) or 'None', 'None')

if __name__ == '__main__':
    unittest.main()
    
