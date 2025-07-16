import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import consts
import urls

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def ad_user(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(urls.MAIN_PAGE_URL)

    enter_btn = wait.until(EC.element_to_be_clickable(Locators.SING_IN_UP_BUTTON))  # Открытие окна авторизации
    enter_btn.click()

    wait.until(EC.visibility_of_element_located(Locators.LOGIN_REGISTRATION_WINDOW))  # Ожидание появления окна авторизации

    email_field = wait.until(EC.visibility_of_element_located(Locators.INPUT_EMAIL))  # Ввод учетных данных
    email_field.send_keys(consts.AD_TEST_EMAIL)

    password_field = wait.until(EC.visibility_of_element_located(Locators.INPUT_PASSWORD))
    password_field.send_keys(consts.AD_TEST_PASSWORD)

    submit_btn = wait.until(EC.element_to_be_clickable(Locators.BUTTON_LOG_IN))   # Отправка формы
    submit_btn.click()

    wait.until(EC.visibility_of_element_located(Locators.USER_TEXT))   # Проверка успешной авторизации
