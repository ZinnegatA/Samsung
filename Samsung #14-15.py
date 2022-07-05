# class Engine:
#     def __init__(self, engine_volume, cylinder_amount, engine_weight):
#         self.engine_volume = engine_volume
#         self.cylinder_amount = cylinder_amount
#         self.engine_weight = engine_weight
#         self.engines = []
#
#     def efficiency(self):
#         return 0.25
#
#     def throttle_energy(self):
#         return self.engine_volume * self.cylinder_amount * 100
#
#     def break_energy(self):
#         return self.engine_weight * 2
#
#     def get_max_speed(self):
#         return (self.throttle_energy() - self.break_energy()) * self.efficiency()
#
#
# class FerrariEngine(Engine):
#     def __init__(self, engine_volume, cylinder_amount, engine_weight):
#         super().__init__(engine_volume, cylinder_amount, engine_weight)
#
#
# class RenaultEngine(Engine):
#     def __init__(self, engine_volume, cylinder_amount, engine_weight, extra_turbo_energy):
#         super().__init__(engine_volume, cylinder_amount, engine_weight)
#         self.extra_turbo_energy = extra_turbo_energy
#
#     def efficiency(self):
#         return 0.27
#
#     def throttle_energy(self):
#         return self.engine_volume * self.cylinder_amount * 110 + self.extra_turbo_energy
#
#     def break_energy(self):
#         return self.engine_weight * 2.1
#
#
# f_eng1 = FerrariEngine(6.3, 12, 85.6)
# f_eng2 = FerrariEngine(6.1, 8, 90.5)
# f_eng3 = FerrariEngine(5.8, 6, 91.2)
# r_eng1 = RenaultEngine(2.4, 4, 56.5, 100.5)
# r_eng2 = RenaultEngine(2.6, 2, 55.4, 99.8)
# r_eng3 = RenaultEngine(1.4, 10, 65.8, 85.1)
#
# engines = Engine(0, 0, 0)
# engines.engines = [f_eng1, f_eng2, f_eng3, r_eng1, r_eng2, r_eng3]
# for eng in engines.engines:
#     print(round(eng.get_max_speed(), 2))

# class User:
#     def __init__(self, id, login, password):
#         self.id = id
#         self.login = login
#         self.password = password
#
#     def get_user_data(self):
#         return f"User ID: {self.id}, Login: {self.login}, Password: {self.password}"
#
#
# class Student(User):
#     def __init__(self, name, surname, group, gpa):
#         self.name = name
#         self.surname = surname
#         self.group = group
#         self.gpa = gpa
#
#     def get_user_data(self):
#         return f"Student name: {self.name}, Student surname: {self.surname}, Student's group: {self.group}, Student's GPA: {self.gpa}"
#
#
# class Teacher(User):
#     def __init__(self, nickname, status, subjects=[]):
#         self.nickname = nickname
#         self.status = status
#         self.subjects = subjects
#
#     def add_subject(self, subject):
#         self.subjects.append(subject)
#
#     def get_user_data(self):
#         return f"Teacher's nickname: {self.nickname}, Status: {self.status}, Subjects: {', '.join(self.subjects)}"
