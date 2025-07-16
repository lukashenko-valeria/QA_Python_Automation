from selenium.webdriver.common.by import By
from consts import ADVERTISEMENT_NAME

class Locators:
    SING_IN_UP_BUTTON = By.XPATH, ".//button[text() = 'Вход и регистрация']"
    LOGIN_REGISTRATION_WINDOW = By.CSS_SELECTOR, ".homePage_modal__zSdUB"
    BUTTON_NO_ACCOUNT = By.XPATH, ".//button[text() = 'Нет аккаунта']"

    REGISTRATION_INPUT_EMAIL = By.XPATH, '//input[contains(@placeholder, "Введите Email")]'
    REGISTRATION_INPUT_PASSWORD = By.XPATH, '//input[contains(@placeholder, "Пароль")]'
    REGISTRATION_REPEAT_PASSWORD = By.XPATH, '//input[contains(@placeholder, "Повторите пароль")]'
    REGISTRATION_POPUP_WINDOW_TEXT = By.XPATH, '//h1[contains(text(), "Зарегистрироваться")]'
    BUTTON_CREATE_ACCOUNT = By.XPATH, ".//button[text() = 'Создать аккаунт']"

    FAILED_EMAIL = By.XPATH, ".//input[@name='email']/ancestor::div[@class='input_inputError__fLUP9']"
    FAILED_PASSWORD = By.XPATH, ".//input[@name='password']/ancestor::div[@class='input_inputError__fLUP9']"
    FAILED_REPEAT_PASSWORD = By.XPATH, ".//input[@name='submitPassword']/ancestor::div[@class='input_inputError__fLUP9']"
    TEXT_ERROR = By.XPATH, '//span[text()="Ошибка"]'

    INPUT_EMAIL = By.NAME, "email"
    INPUT_PASSWORD = By.NAME, "password"
    BUTTON_LOG_IN = By.XPATH, ".//button[text() = 'Войти']"
    USER_TEXT = By.XPATH, ".//h3[text()='User.']"
    BUTTON_LOG_OUT = By.XPATH, ".//button[text() = 'Выйти']"
    PROFILE_ICON = By.CLASS_NAME, "svgSmall"


class AdvertLocators:
    TXT_ERROR = By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    CREATE_AD_BTN = By.XPATH, "//*[text()='Разместить объявление']"
    AUTH_REQUIRED_POPUP = By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    NEW_AD_HEADER = By.XPATH, "//h1[text()='Новое объявление']"
    AD_NAME_INPUT = By.XPATH, "//input[@name='name']"
    FILLED_AD_NAME = By.XPATH, "//input[@value='Гарри Поттер']"
    CATEGORY_DROPDOWN = By.XPATH, "//div[@class='dropDownMenu_input__itKtw' and .//input[@name='category']]/button"
    BOOKS_CATEGORY = By.XPATH, "//button[span[text()='Книги']]"
    USED_CONDITION = By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']"
    CITY_DROPDOWN = By.XPATH, "//div[@class='dropDownMenu_input__itKtw' and .//input[@name='city']]/button"
    SPB_CITY = By.XPATH, "//button[span[text()='Санкт-Петербург']]"
    DESCRIPTION_INPUT = By.XPATH, "//textarea[@name='description']"
    PRICE_INPUT = By.XPATH, "//input[@name='price']"
    PUBLISH_BTN = By.XPATH, "//button[text()='Опубликовать']"
    UPLOADED_IMAGE = By.XPATH, '//img[@class="picture"]'
    PUBLISHED_AD = By.XPATH, f"//h2[contains(text(), '{ADVERTISEMENT_NAME}')]"
