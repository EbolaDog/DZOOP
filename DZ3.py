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
            
    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[])))
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            return ('Ошибка')
        return self.average < other.average

    def __str__(self):
        return (f'Студент\n'
        f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {round(self.average_grade(), 2)}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {",".join(self.finished_courses)}\n')
         
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        self.average_grade = sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[]))
        return self.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return ('Ошибка')
        return self.average_grade < other.average_grade

    def __str__(self):
        return (f'Лектор\n'
        f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {round(self.average_grade(), 2)}\n')

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

    def __str__(self):
        return (f'Рецензент\n'
        f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
 
liza_lecturer = Lecturer('Liza', 'Buddy')
liza_lecturer.courses_attached += ['Python']

Vasya_reviewer = Reviewer('Vasya', 'Okyshkin')
Vasya_reviewer.courses_attached += ['Python']

Vasya_reviewer.rate_student(best_student, 'Python', 10)
Vasya_reviewer.rate_student(best_student, 'Python', 8)
best_student.rate_lecturer(liza_lecturer, 'Python', 8)

print(best_student)
print(Vasya_reviewer)
print(liza_lecturer)
