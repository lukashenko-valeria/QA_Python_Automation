from faker import Faker

fake = Faker(locale="ru_RU")  #  генератор по России

def generated_email():
    return fake.email()

def generated_password(length=10):
    return fake.password(length=length, special_chars=False)

def generated_first_name():
    return fake.first_name()

def generated_last_name():
    return fake.last_name()

def generated_login():
    return fake.user_name()





