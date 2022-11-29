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


kowka = Employee (1, "Kowka K.S", "13.13.1313", 666)
print(kowka)



