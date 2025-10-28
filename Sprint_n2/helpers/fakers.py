from faker import Faker

fake = Faker(locale="ru_RU")  #  генератор по России

def generated_email():
    return fake.email()

def generated_password(length=10):
    return fake.password(length=length, special_chars=False)

def generate_user_data():
    password = generated_password()  # создаем пароль один раз
    return {
        'email': generated_email(),
        'password': password,
        'submitPassword': password  # используем тот же пароль
    }
