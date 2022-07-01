from enum import Enum


class Employee:
    def __init__(self, name, role, department, salary, year):
        self.name = name
        self.role = role
        self.department = department
        self.salary = salary
        self.year = year

    def __repr__(self):
        return f'Сотрудник {self.name}, {self.department}'


class Car:
    def __init__(self, model, cost, type, year):
        self.model = model
        self.cost = cost
        self.type = type
        self.year = year

    def __repr__(self):
        return f'Модель машины: {self.model}, цена: {self.cost}'


class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def add_emp(self, *args):
        self.employees.extend(args)

    def __repr__(self):
        return self.name


class Role(Enum):
    DIRECTOR = 1
    ENGINEER = 2
    MANAGER = 3
    CLEANER = 4
    SECURITY = 5


class CarType(Enum):
    SEDAN = 1
    SUPERCAR = 2
    SPORT_CAR = 3
    OFF_ROAD = 4
    MINIVAN = 5


class Company:
    def __init__(self, name, departments, cars):
        self.name = name
        self.departments = departments
        self.cars = cars

    def add_dep(self, *args):
        self.departments.extend(args)

    def add_car(self, *args):
        self.cars.extend(args)

    def total_cars_price(self):
        return sum([car.cost for car in self.cars])

    def avg_salary(self):
        total = 0
        emps = 0
        for dep in self.departments:
            for emp in dep.employees:
                total += emp.salary
                emps += 1
        return int(total / emps)

    def give_prem(self):
        for dep in self.departments:
            for emp in dep.employees:
                if emp.year > 5:
                    print(f'Сотруднику {emp.name} положена премия!')
        return "Поздравляем!"

    def cars_rating(self):
        return sorted(self.cars, key=lambda x: x.cost)

    def move_emp(self, from_dep_indx, to_dep_indx, emp_indx):
        employee = self.departments[from_dep_indx].employees.pop(emp_indx)
        self.departments[to_dep_indx].employees.append(employee)


dep1 = Department('Департамент управления', [])
dep2 = Department('Департамент инженерного обеспечения', [])
dep3 = Department('Департамент администрации', [])
emp1 = Employee('Имя1', Role.DIRECTOR, dep1, 100000, 5)
emp2 = Employee('Имя2', Role.MANAGER, dep1, 70000, 3)
emp3 = Employee('Имя3', Role.ENGINEER, dep2, 80000, 10)
emp4 = Employee('Имя4', Role.CLEANER, dep3, 50000, 2)
emp5 = Employee('Имя5', Role.SECURITY, dep3, 60000, 6)
dep1.add_emp(emp1, emp2)
dep2.add_emp(emp3)
dep3.add_emp(emp4, emp5)
car1 = Car('Mercedes', 1500000, CarType.SUPERCAR, 2015)
car2 = Car('Volkswagen', 100000, CarType.MINIVAN, 2011)
car3 = Car('Ferrari', 2500000, CarType.SPORT_CAR, 2020)
car4 = Car('Tesla', 1000000, CarType.SEDAN, 2021)
car5 = Car('Nissan', 800000, CarType.OFF_ROAD, 2008)
company = Company('Astana Motors', [], [])
company.add_car(car1, car2, car3, car4, car5)
company.add_dep(dep1, dep2, dep3)

print(f"""Общая стоимость машин в комании: {company.total_cars_price()})
Средняя зарплата по заводу: {company.avg_salary()}
Рейтинг машин по возрастанию цены: {company.cars_rating()}
Рейтинг машин по убыванию цены: {company.cars_rating()[::-1]}""")
print(dep1.__dict__)
print(dep2.__dict__)
company.move_emp(0, 1, 0)
print(dep1.__dict__)
print(dep2.__dict__)

print(company.give_prem())
