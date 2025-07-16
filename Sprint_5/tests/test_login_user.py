from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
import consts
import urls

class TestLoginAndLogout:

    def test_user_login(self, driver):
        driver.get(urls.MAIN_PAGE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))  # Задаем ожидание на поиск кнопки "Вход и регистрация"
        driver.find_element(*Locators.SING_IN_UP_BUTTON).click()  # Найти кнопку "Вход и регистрация" и кликнуть на нее
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW)) # Задаем ожидание для появления модального окна
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(consts.STD_TEST_EMAIL)  # Ввести адрес электронной почты
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD)  # Ввести пароль

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_LOG_IN)) # Задаем ожидание на поиск кнопки "Войти"
        driver.find_element(*Locators.BUTTON_LOG_IN).click()  # Найти кнопку "Войти" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.USER_TEXT)) # Задаем ожидание на поиск надписи User.
        user_name = driver.find_element(*Locators.USER_TEXT).text
        assert user_name == "User."
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PROFILE_ICON))

    def test_user_logout(self, driver):
        driver.get(urls.MAIN_PAGE_URL)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))  # Задаем ожидание на поиск кнопки "Вход и регистрация"
        driver.find_element(*Locators.SING_IN_UP_BUTTON).click()  # Найти кнопку "Вход и регистрация" и кликнуть на нее
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW))  # Задаем ожидание для появления модального окна
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(consts.STD_TEST_EMAIL)  # Ввести адрес электронной почты
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(consts.STD_TEST_PASSWORD)  # Ввести пароль

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_LOG_IN)) # Задаем ожидание на поиск кнопки "Войти"
        driver.find_element(*Locators.BUTTON_LOG_IN).click()  # Найти кнопку "Войти" и кликнуть на нее

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.BUTTON_LOG_OUT))
        driver.find_element(*Locators.BUTTON_LOG_OUT).click()  # Найти кнопку "Выйти" и кликнуть на нее
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))
        button_name = driver.find_element(*Locators.SING_IN_UP_BUTTON).text
        assert button_name == "Вход и регистрация"
        assert WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(Locators.USER_TEXT))
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SING_IN_UP_BUTTON))
