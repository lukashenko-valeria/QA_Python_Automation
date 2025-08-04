from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_SCOOTER = (By.XPATH, "//div[contains(@class, 'Header_Logo')]/a")
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")
