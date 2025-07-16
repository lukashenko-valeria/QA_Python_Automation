from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import consts
import urls
import helpers

class TestRegistration:

    def test_user_registration_correct_email(self, driver):
        driver.get(urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON)) # Задаем ожидание на поиск кнопки "Вход и регистрация"
        driver.find_element(*Locators.SING_IN_UP_BUTTON).click() # Найти кнопку "Вход и регистрация" и кликнуть на нее
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW)) # Задаем ожидание для появления модального окна
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_NO_ACCOUNT)) # Задаем ожидание на поиск кнопки "Нет аккаунта"
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click() # Найти кнопку "Нет аккаунта" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_POPUP_WINDOW_TEXT))

        user_email = helpers.get_random_email()
        user_password = "registered_password"

        driver.find_element(*Locators.REGISTRATION_INPUT_EMAIL).send_keys(user_email)
        driver.find_element(*Locators.REGISTRATION_INPUT_PASSWORD).send_keys(user_password)
        driver.find_element(*Locators.REGISTRATION_REPEAT_PASSWORD).send_keys(user_password)
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT ).click()
        #time.sleep(15)
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(Locators.USER_TEXT))
        user_name = driver.find_element(*Locators.USER_TEXT).text
        assert user_name == "User."

    def test_user_registration_failed_email(self, driver):
        driver.get(urls.MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))  # Задаем ожидание на поиск кнопки "Вход и регистрация"
        driver.find_element(*Locators.SING_IN_UP_BUTTON).click()  # Найти кнопку "Вход и регистрация" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW))  # Задаем ожидание для появления модального окна
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_NO_ACCOUNT))  # Задаем ожидание на поиск кнопки "Нет аккаунта"
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click()  # Найти кнопку "Нет аккаунта" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_POPUP_WINDOW_TEXT))

        driver.find_element(*Locators.REGISTRATION_INPUT_EMAIL).send_keys(consts.WRONG_TEST_EMAIL)
        driver.find_element(*Locators.REGISTRATION_INPUT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD)
        driver.find_element(*Locators.REGISTRATION_REPEAT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD)
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FAILED_EMAIL))
        input_email = driver.find_element(*Locators.FAILED_EMAIL)
        assert input_email.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        input_password = driver.find_element(*Locators.FAILED_PASSWORD)
        assert input_password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        input_repeat_password = driver.find_element(*Locators.FAILED_REPEAT_PASSWORD)
        assert input_repeat_password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ERROR))
        assert driver.find_element(*Locators.TEXT_ERROR)

    def test_user_exist_registration(self, driver):
        driver.get(urls.MAIN_PAGE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))  # Задаем ожидание на поиск кнопки "Вход и регистрация"
        driver.find_element(*Locators.SING_IN_UP_BUTTON).click()  # Найти кнопку "Вход и регистрация" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW))  # Задаем ожидание для появления модального окна
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_NO_ACCOUNT))  # Задаем ожидание на поиск кнопки "Нет аккаунта"
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click()  # Найти кнопку "Нет аккаунта" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_POPUP_WINDOW_TEXT))

        driver.find_element(*Locators.REGISTRATION_INPUT_EMAIL).send_keys(consts.STD_TEST_EMAIL) # Вводим аккаунт уже зарегистрированного пользователя
        driver.find_element(*Locators.REGISTRATION_INPUT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD) # Вводим пароль
        driver.find_element(*Locators.REGISTRATION_REPEAT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD) # Появторяем пароль
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.FAILED_EMAIL))
        input_email = driver.find_element(*Locators.FAILED_EMAIL)
        assert input_email.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        input_password = driver.find_element(*Locators.FAILED_PASSWORD)
        assert input_password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        input_repeat_password = driver.find_element(*Locators.FAILED_REPEAT_PASSWORD)
        assert input_repeat_password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.TEXT_ERROR))
        assert driver.find_element(*Locators.TEXT_ERROR)
