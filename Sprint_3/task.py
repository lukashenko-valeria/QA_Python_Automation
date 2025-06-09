import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if not name or len(name) > 40:
           raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
           raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not  in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price[item])
        result = sum(total)
        if len(self.__name_items) > 10:
            result *= 0.9
        return result

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item_name in self.__name_items:
            tax_rate = self.__tax_rate[item_name]
            price = self.__item_price[item_name]
            if tax_rate == 20:
                twenty_percent_tax.append(item_name)
                total.append(price)
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9
        return total_sum * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item_name in self.__name_items:
            tax_rate  = self.__tax_rate[item_name]
            price = self.__item_price[item_name]
            if tax_rate == 10:
                ten_percent_tax.append(item_name)
                total.append(price)
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum *= 0.9
        return total_sum * 0.1

    def total_tax(self):
        return  self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        str_number = str(telephone_number)
        if len(str_number) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{str_number}'

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [ ['часы', lambda x: x.hour],
                 ['минуты', lambda x: x.minute],
                 ['день', lambda x: x.day],
                 ['месяц', lambda x: x.month],
                 ['год', lambda x: x.year]
               ]
        for time_list in date:
            time_mark = time_list[0]
            time_value = time_list[1](now)
            date_and_time.append(f'{time_mark}: {time_value}')
        return date_and_time


# 1. Проверяем чтение свойств name_items и number_items(
check = OnlineSalesRegisterCollector()
print(check.name_items)
print(check.number_items)

# 2. Проверка добавления товаров в чек
#Позитивная проверка
check.add_item_to_cheque('молоко')
print(check.name_items)
print(check.number_items)

#Негативная проверка - отсутствует в справочнике товаров
try:
    check.add_item_to_cheque('сигареты')
except NameError as e:
    print(e)
    print("Сработала проверка товара, отсутствующего в списке")

#Негативная проверка - неверная длина товара
try:
    check.add_item_to_cheque('')
except ValueError as e:
    print(e)
    print("Сработала проверка товара, некорректного по длине названия")

# 3. Проверка на удаление товара
check.delete_item_from_check('молоко')
print(check.name_items)
print(check.number_items)

try:
    check.delete_item_from_check('вода')
except NameError as e:
    print(e)
    print("Сработала проверка: 'Позиция отсутствует в чеке'")

# 4. Проверка суммы чека
check.add_item_to_cheque('молоко')
check.add_item_to_cheque('кефир')
print(check.check_amount())

# 5. Проверка НДС 20%
check.add_item_to_cheque('чипсы')
check.add_item_to_cheque('кола')
print(check.twenty_percent_tax_calculation())

# 6. Проверка НДС 10%
check.add_item_to_cheque('молоко')
check.add_item_to_cheque('кефир')
print(check.name_items)
print(check.ten_percent_tax_calculation())

# 7. Проверка суммы налогов
print(check.total_tax())

# 8. Проверка номера телефона
# Позитивная проверка
print(check.get_telephone_number(1234567890))
#Негативная проверка
try:
    print(check.get_telephone_number(1234567891110))
except ValueError as e:
    print(e)
    print("Сработала проверка на неверную длину номера телефона")

# 9. Проверка статического метода get_date_and_time
# Он возвращает дату и время покупки в таком формате: ['часы: 13', 'минуты: 31', 'день: 10', 'месяц: 7', 'год: 2023']
print(check.get_date_and_time())
