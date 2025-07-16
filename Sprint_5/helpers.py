import random
import time

def get_random_email():
    random.seed(time.time())  # Инициализация датчика случайных чисел текущим временем
    some_digits = random.randint(1, 999999999)  # Генерируем случайное число от 1 до 999999999
    return f"v.lukashenko{some_digits}@gmail.com"
