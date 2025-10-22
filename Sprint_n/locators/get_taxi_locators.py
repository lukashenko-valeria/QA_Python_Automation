from selenium.webdriver.common.by import By


class GetTaxiLocators:

    # кнопка Вызвать и заказать
    BUTTON_CALL_NUMBER = (By.XPATH, ".//span[@class = 'smart-button-main']") # перенести

    # Локатор для получения списка тарифов
    TAXI_TARIFFS = (By.XPATH, ".//div[@class='tcard-title']")

    INFO_BUTTON_I = (By.XPATH, ".//div[@class='tcard active']/button[@class = 'i-button tcard-i active']") # кнопка информации i
    ACTIVE_TITLE = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-title']")
    ACTIVE_DESCRIPTION = (By.XPATH, ".//div[@class='tcard active']//div[@class = 'i-dPrefix']")

    # Поля с дополнительной информацией
    TEXT_PHONE_FIELD = (By.CLASS_NAME, "np-text")
    TEXT_PAYMENT_INFO = (By.CLASS_NAME, "pp-text")
    TEXT_COMMENT_FIELD = (By.XPATH, ".//input[@id='comment']/../label")
    TEXT_REQUIREMENTS = (By.CLASS_NAME, 'reqs-head')
    TEXT_GET_TAXI_BUTTON = (By.CLASS_NAME, "smart-button-main")

    TEXT_EXTRA_WISHES_REQS_ARROW = (By.CLASS_NAME, 'reqs-arrow')
    EXTRA_INFO_PANEL = (By.XPATH, ".//*[@class='tariff-picker shown']")
    EXTRA_INFO_LAPTOP_CHECKBOX = (By.XPATH, ".//*[@class='slider round']")
