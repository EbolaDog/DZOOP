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
        self.average = round(sum(sum(self.grades.values(),[]))/len(sum(self.grades.values(),[])))
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return ('Ошибка')
        return self.average < other.average

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
maxim_student = Student('Maxim', 'Melnikov', 'your_gender')
maxim_student.courses_in_progress += ['Python']
 
liza_lecturer = Lecturer('Liza', 'Buddy')
liza_lecturer.courses_attached += ['Python']
Viktor_lecturer = Lecturer('Viktor', 'Zyev')
Viktor_lecturer.courses_attached += ['Python']

Vasya_reviewer = Reviewer('Vasya', 'Okyshkin')
Vasya_reviewer.courses_attached += ['Python']
Nastya_reviewer = Reviewer('Nastya', 'Klimova')
Nastya_reviewer.courses_attached += ['Python']

Vasya_reviewer.rate_student(best_student, 'Python', 10)
Nastya_reviewer.rate_student(best_student, 'Python', 8)
Vasya_reviewer.rate_student(maxim_student, 'Python', 7)
Nastya_reviewer.rate_student(maxim_student, 'Python', 9)
best_student.rate_lecturer(liza_lecturer, 'Python', 8)
maxim_student.rate_lecturer(Viktor_lecturer, 'Python', 10)
best_student.rate_lecturer(Viktor_lecturer, 'Python', 7)
maxim_student.rate_lecturer(liza_lecturer, 'Python', 10)

best_student.average_grade()
maxim_student.average_grade()
print(maxim_student < best_student)
print(best_student)

liza_lecturer.average_grade()
Viktor_lecturer.average_grade()
print(liza_lecturer < Viktor_lecturer)
print(liza_lecturer)

student_list = [maxim_student, best_student]
subject_python_student = []
for student in student_list:
    for subject, grade in student.grades.items():
        subject_python_student.append(grade)
s_python = sum(sum(subject_python_student,[]))/len(sum(subject_python_student,[]))  

lecturer_list = [liza_lecturer, Viktor_lecturer]
subject_python_lecturer = []
for lecturer in lecturer_list:
    for subject, grade in lecturer.grades.items():
        subject_python_lecturer.append(grade)
l_python = sum(sum(subject_python_lecturer,[]))/len(sum(subject_python_lecturer,[]))  

print(Vasya_reviewer)
print(f'Средняя оценка за домашее задание по "Python" всех студентов: {s_python}') 
print(f'Средняя оценка за лецкии в рамках курса "Python": {l_python}') 
