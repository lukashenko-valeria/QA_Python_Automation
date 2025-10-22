from selenium.webdriver.common.by import By


class OrderTaxiLocators:
    TAXI_TITLE = (By.XPATH, ".//*[@class='order-header-title']")
    TIMER = (By.XPATH, ".//*[@class='order-header-time']")
    CANCEL_BUTTON = (By.XPATH, ".//div[text()='Отменить']/../button")
    CANCEL_BUTTON_TEXT = (By.XPATH, ".//div[text()='Отменить']")
    DETAILS_BUTTON = (By.XPATH, ".//div[text()='Детали']/../button")
    DETAILS_BUTTON_TEXT = (By.XPATH, ".//div[text()='Детали']")

    TRIP_COST = (By.XPATH, ".//div[contains(text(), 'Стоимость') or contains(@class, 'cost')]")

    DETAILS_PANEL = (By.XPATH, ".//div[contains(@class, 'details') or contains(@class, 'trip-info')]")

    ADDITIONAL_INFO_TITLE = (By.XPATH,
                             ".//div[contains(text(), 'Еще про поездку') or contains(@class, 'additional-info')]")
