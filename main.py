#####################DATE####################
import datetime as dt

def str_to_date(self_date, other_date):
    dt1 = self_date.split('.')
    dt2 = other_date.split('.')
    self_date = dt.date(int(dt1[2]),int(dt1[1]),int(dt1[0]))
    other_date = dt.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_date, other_date


################ZP####################
class Employee:
    def __init__(self, number, fio, bdate, oklad, on_leave=False):
        self.number = number
        self.fio = fio
        self.bdate = bdate
        self.oklad = oklad
        self.on_leave = on_leave

    def increase_salary(self, summa):
        self.oklad += summa

    def __str__(self):
        return f"Сотрудник {self.number} {self.fio} {self.bdate} оклад: {self.oklad}, в отпуске: " \
               f"{'да' if self.on_leave else 'нет'}"

    def __lt__(self, other):   #<
        self_bdate, other_bdate = str_to_date(self.bdate,other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):   #==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):   #<=
        if self.__eq__(other):
            return True
        if self.__lt__(other):
            return  True
        else:
            return False

###################NA4ALNIK#######################
class Department:
    def __init__(self, title, chief=None, employees=None):
        self.title = title
        if employees is None:
            employees = list()
        self.employees = employees
        self.chief = chief

    def append (self, emp):
        self.employees.append(emp)

    def __str__(self):
        return f"Отдел: {self.title}, начальник: ,{self.chief} кол-во сотрудников: {len(self.employees)}"

    def print_employees(self):
        for emp in self.employees:
            print(emp)

    def print_employees_on_leave(self, status=True):
        for emp in self.employees:
            if emp.on_leave == status:
                print(emp)



kowka = Employee (1, "Kowka K.S", "13.12.1313", 666)
kisja = Employee (2, "Kisja K.I", "15.12.1314", 999, True)
foxy = Employee (3, "Foxy N.T", "14.12.1315", 6969, True)
print(kisja == kowka)
print(kisja >= kowka)
print(kisja > kowka)


arhive = Department("Архив", employees=[kowka])
arhive.append(kisja)
arhive.append(foxy)
arhive.print_employees_on_leave(False)