
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _homework_average_score_(self):
        list_all_score = list()
        for score in self.grades.values():
            list_all_score += score
        return sum(list_all_score) / len(list_all_score)

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            return f'{other_student.name} не является студентом'
        elif self._homework_average_score_() > other_student._homework_average_score_():
            return f'Средняя оценка за домашнее задание у {self.surname} {self.name} лучше чем у {other_student.surname} {other_student.name}'
        else:
            return f'Средняя оценка за домашнее задание у {other_student.surname} {other_student.name} лучше чем у {self.surname} {self.name}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._homework_average_score_()}\
        \nКурсы в процессе изучения: {", ".join(map(str,self.courses_in_progress))}\nЗавершенные курсы: {", ".join(map(str,self.finished_courses))}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _average_score_(self):
        list_all_score = list()
        for score in self.grades.values():
            list_all_score += score
        return sum(list_all_score) / len(list_all_score)

    def __lt__(self, other_lectorer):
        if not isinstance(other_lectorer, Lecturer):
            return f'{other_lectorer.name} не является лектором'
        elif self._average_score_() > other_lectorer._average_score_():
            return f'У лектора {self.surname} {self.name} средняя оценка за лекции лучше чем у {other_lectorer.surname} {other_lectorer.name}'
        else:
            return f'У лектора {other_lectorer.surname} {other_lectorer.name} средняя оценка за лекции лучше чем у {self.surname} {self.name}'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_score_()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def everage_score_for_homework(student_list, course):
    list_all_score = list()
    for current_student in student_list:
        for courses_in_progress, score_for_courses in current_student.grades.items():
            if course in courses_in_progress:
                list_all_score += score_for_courses
    if len(list_all_score) > 0:
        print(f'Средняя оценка по курсу {course}: {sum(list_all_score) / len(list_all_score)}')
    else:
        print(f'Студенты не изучали курс - {course}')

def everage_score_for_lecture(lecturer_list, course):
    list_all_score = list()
    for current_lecturer in lecturer_list:
        for courses_attached, score_for_courses in current_lecturer.grades.items():
            if course in courses_attached:
                list_all_score += score_for_courses
    if len(list_all_score) > 0:
        print(f'Средняя оценка по лекции {course}: {sum(list_all_score) / len(list_all_score)}')
    else:
        print(f'Лектор не читал курс - {course}')

best_student_1 = Student('Ruoy', 'Eman', 'male')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['C#']
best_student_1.finished_courses += ['Assembler']

best_student_2 = Student('Kasandra', 'Clon', 'female')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['C#']
best_student_2.finished_courses += ['Basic']


example_Reviewer_1 = Reviewer('Ivan', 'Ivanov')
example_Reviewer_1.courses_attached += ['Python']

example_Reviewer_1.rate_hw(best_student_1, 'Python', 10)
example_Reviewer_1.rate_hw(best_student_2, 'Python', 9)

example_Reviewer_2 = Reviewer('Petr', 'Petrov')
example_Reviewer_2.courses_attached += ['C#']

example_Reviewer_2.rate_hw(best_student_1, 'C#', 10)
example_Reviewer_2.rate_hw(best_student_2, 'C#', 7)


example_Lecturer_1 = Lecturer('Vasilyi', 'Sidorov')
example_Lecturer_1.courses_attached += ['Python']

example_Lecturer_2 = Lecturer('Nikolay', 'Smith')
example_Lecturer_2.courses_attached += ['C#']

best_student_1.rate_hw(example_Lecturer_1, 'Python', 9)
best_student_2.rate_hw(example_Lecturer_1, 'Python', 8)

best_student_1.rate_hw(example_Lecturer_2, 'C#', 8)
best_student_2.rate_hw(example_Lecturer_2, 'C#', 7)

print(best_student_1)
print(best_student_2)
print(best_student_1 >best_student_2)

print(example_Lecturer_1)
print(example_Lecturer_2)
print(example_Lecturer_1 > example_Lecturer_2)

print(example_Reviewer_1)
print(example_Reviewer_2)

list_student = list()
list_student.append(best_student_1)
list_student.append(best_student_2)

everage_score_for_homework(list_student, 'Python')

list_lecturer = list()
list_lecturer.append(example_Lecturer_1)
list_lecturer.append(example_Lecturer_2)

everage_score_for_lecture(list_lecturer, 'C#')