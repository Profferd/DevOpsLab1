from Models.StudentRepo import StudentRepo
from Models.SubjectRepo import SubjectRepo
from Models.score import Score

students = StudentRepo()
subjects = SubjectRepo()

def show_menu():
    print('To quit press Ctrl-C')
    print('Available commands:')
    print('----Subject----')
    print('1 - add new subject')
    print('2 - get all subjects')
    print('3 - find the subject')
    print('4 - update the subject')
    print('5 - remove the subject')
    print('----Student----')
    print('6 - add new student')
    print('7 - get all students')
    print('8 - find the student')
    print('9 - remove the student')
    print('-----Score-----')
    print('10 - add score to the student')

def create_subject():
    name = input('Enter a name of the subject: ')
    passing_score = int(input('Enter a passing score of the subject: '))
    if subjects.create_subject(name, passing_score):
        print('Subject was created successfully!')
    else:
        print('Subject with such name already exists!')

def get_subjects():
    print('\n'.join(map(str, subjects.get_subjects())) or 'None')

def find_subject():
    name = input('Enter a name of the subject: ')
    index = subjects.find_subject(name)
    if index == -1:
        raise Exception('Subject with such name doesn\'t exist!')
    subject = subjects.get_subjects()[index]
    print(f'Found subject: {subject}')
    print('List of students that attends this subject:')
    print('\n'.join(map(str, subject.get_students())) or 'None')

def update_subject():
    name = input('Enter a name of the subject: ')
    passing_score = int(input('Enter new passing score of the subject: '))
    if not subjects.update_subject(name, passing_score):
        raise Exception('Subject with such name doesn\'t exist!')
    print('Subject was updated successfully!')

def delete_subject():
    name = input('Enter a name of the subject: ')
    if not subjects.delete_subject(name):
        raise Exception('Subject with such name doesn\'t exist!')
    print('Subject was removed successfully!')

def create_student():
    first_name = input('Enter first name of the student: ')
    last_name = input('Enter last name of the student: ')
    if not students.create_student(first_name, last_name):
        raise Exception('Student with such first or last name already exists!')
    print('Student was created successfully!')

def get_students():
    print('\n'.join(map(str, students.get_students())) or 'None')
    
def find_student():
    first_name = input('Enter first name of the student: ')
    last_name = input('Enter last name of the student: ')
    index = students.find_student(first_name, last_name)
    if index == -1:
        raise Exception('Student with such first or last name doesn\'t exist!')
    student = students.get_students()[index]
    print(f'Student\'s GPA: {student.gpa()}')
    print('Student attends:')
    print('\n'.join(map(str, student.subjects())) or 'None')
    print('Student passed:')
    print('\n'.join(map(str, student.passed_subjects())) or 'None')
    
def delete_student():
    first_name = input('Enter first name of the student: ')
    last_name = input('Enter last name of the student: ')
    if not students.delete_student(first_name, last_name):
        raise Exception('Student with such first or last name doesn\'t exist!')
    print('Student was deleted successfully!')

def add_score():
    name = input('Enter a name of the subject: ')
    subj_index = subjects.find_subject(name)
    if subj_index == -1:
        raise Exception('Subject with such name doesn\'t exist!')
    subject = subjects.get_subjects()[subj_index]
    first_name = input('Enter first name of the student: ')
    last_name = input('Enter last name of the student: ')
    stud_index = students.find_student(first_name, last_name)
    if stud_index == -1:
        raise Exception('Student with such first or last name doesn\'t exist!')
    student = students.get_students()[stud_index]
    score_value = int(input('Enter score of the student: '))
    score = Score(student, subject, score_value)
    student.get_scores().append(score)
    subject.get_scores().append(score)
    print('Score was added successfully!')

def execute(command):
    command = int(command)
    commands = {
        1: create_subject,
        2: get_subjects,
        3: find_subject,
        4: update_subject,
        5: delete_subject,
        6: create_student,
        7: get_students,
        8: find_student,
        9: delete_student,
        10: add_score
    }
    if command not in commands:
        raise Exception('Wrong command! Try again.')
    commands[command]()


if __name__ == '__main__':
    while True:
        show_menu()
        try:
            execute(input('Enter command: '))
        except Exception as e:
            print(e)

        