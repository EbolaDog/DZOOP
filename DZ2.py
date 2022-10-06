class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)   

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
liza_lecturer = Lecturer('Some', 'Buddy')
liza_lecturer.courses_attached += ['Python']

Vasya_reviewer = Reviewer('Vasya', 'Okyshkin')
Vasya_reviewer.courses_attached += ['Python']

Vasya_reviewer.rate_student(best_student, 'Python', 10)
Vasya_reviewer.rate_student(best_student, 'Python', 10)
Vasya_reviewer.rate_student(best_student, 'Python', 10)
best_student.rate_lecturer(liza_lecturer, 'Python', 9)


print(best_student.grades)
print(liza_lecturer.grades)