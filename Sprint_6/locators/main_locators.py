from selenium.webdriver.common.by import By


class MainLocators:
    # Вопросы
    COOKIE = [By.XPATH, "//button[text()='да все привыкли']"]
    QUESTION = (By.XPATH, '//div[@id="accordion__heading-{}"]')
    ANSWER = (By.XPATH, '//div[@id="accordion__panel-{}"]')
    SCROLL_TO_QUESTION = (By.XPATH, '//div[@id="accordion__heading-7"]') #
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_LOW = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
