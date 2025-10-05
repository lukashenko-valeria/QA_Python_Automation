from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, 'password')
    ENTER_BUTTON_CREATE = (By.XPATH, "//a[contains(text(), 'Создать аккаунт')]") # нажимаем на кнопку Создать аккаунт

    NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    LOGIN = (By.NAME, "username")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, 'password')
    ENTER_BUTTON_CREATE_LOW = By.XPATH, "//button[text()='Создать аккаунт']"
    CREATE_ACCOUNT_BUTTON = (By.TAG_NAME, "button")
    TITLE = (By.TAG_NAME, "h1") # Заголовок на странице Войти на сайт

    ENTER_BUTTON_SIGNIN = (By.CSS_SELECTOR, "button.style_button__1FFWl.styles_button__1jD3X.style_button_style_dark-blue__1cpq7")
    BUTTON_EXIT = (By.XPATH, ".//*[text()='Выход']")


