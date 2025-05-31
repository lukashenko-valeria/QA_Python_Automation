class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
       cls.hourly_payment = hourly_payment

    def salary(self):
        salary = self.hours * self.hourly_payment
        return (salary)


# Проверка метода set_hourly_payment
worker = EmployeeSalary('Masha', 2, "", "m@maul.ru")
worker.set_hourly_payment(10)
print('hourly_payment =', worker.hourly_payment)

# Проверка метода get_hours
worker = EmployeeSalary.get_hours('Masha', 2, "")
print('hours =', worker.hours)

# Проверка метода get_email
worker = EmployeeSalary.get_email('Masha', 8, 2)
print('email = ', worker.email)

# Проверка метода salary
print('salary =', worker.salary())

