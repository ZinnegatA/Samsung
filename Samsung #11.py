# class Student:
#     def __init__(self, name, surname, gpa):
#         self.name = name
#         self.surname = surname
#         self.gpa = gpa
#
#     def getStudentData(self):
#         return f'Имя студента: {self.name}, Фамилия студента: {self.surname}, GPA студента: {self.gpa}'
#
#     @staticmethod
#     def topStudent(grades):
#         return max(grades, key=lambda x: x.gpa)
#
#
# student1 = Student('John', 'Lennon', 3.0)
# student2 = Student('Kurt', 'Cobain', 3.5)
# student3 = Student('Alisher', 'Usmanov', 3.2)
# student4 = Student('Oleg', 'Tinkoff', 4.0)
# student5 = Student('Timur', 'Ibragimov', 3.7)
# student6 = Student('John', 'Johnson', 3.8)
# student7 = Student('Donald', 'Trump', 2.4)
# student8 = Student('Khabib', 'Nurmagamedov', 3.9)
# student9 = Student('Oleg', 'Tabakov', 1.8)
# student10 = Student('Ruslan', 'Ibragimov', 2.1)
#
# students = [student1, student2, student3, student4, student5, student6, student7, student8, student9, student10]
# for student in students:
#     print(student.getStudentData())
#
# print(Student.topStudent(students).getStudentData())
#
#
# def add_student(name, surname, gpa):
#     students.append(Student(name, surname, gpa))
#
#
# while True:
#     button = int(input('''PRESS [1] TO ADD STUDENT
# PRESS [2] TO LIST STUDENT
# PRESS [0] TO EXIT
#     '''))
#
#     if button == 1:
#         add_student(input('Name: '), input('Surname: '), input('GPA: '))
#     elif button == 2:
#         for student in students:
#             print(student.getStudentData())
#     elif button == 0:
#         exit()
#     else:
#         print('Error')
