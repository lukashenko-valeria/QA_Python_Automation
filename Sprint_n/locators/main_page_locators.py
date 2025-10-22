from selenium.webdriver.common.by import By


class MainLocators:
    # Поля "Куда" и "Откуда"
    FROM_LOCATOR = (By.ID, "from")
    END_LOCATOR = (By.ID, "to")

    POINTS = (By.XPATH, ".//ymaps[contains(@class, 'ymaps-2-1-79-route-pin__text')]/ymaps[@id]") # Точки начала и конца маршрута на карте
    ROUTE_PANEL = (By.XPATH, ".//div[@class='type-picker shown']") # панель маршрута на карте

    FREE_CAR = (By.XPATH, ".//div[@class='text' and text()='Авто Бесплатно']")
    FREE_DURATION = (By.XPATH, ".//div[@class='duration' and text()='В пути 0 мин.']")

    ROUTE_DESCRIPTION_TEXT_LOCATOR = (By.CLASS_NAME, "text")
    ROUTE_TAB = (By.XPATH, ".//div[@class='modes-container']/div[contains(@class, 'mode')]") # вкладки - маршруты - получаем список вкладок

    # Текст на вкладке маршрута Быстрый
    TEXT_CAR = (By.CLASS_NAME, "text")
    DURATION_CAR = (By.CLASS_NAME, "duration")

    # Вкладки маршрута
    OPTIM = (By.XPATH, ".//div[@class='mode' and text()='Оптимальный']")
    FAST = (By.XPATH, ".//div[@class='mode active' and text()='Быстрый']")
    OWN = (By.XPATH, ".//div[@class='mode' and text()='Свой']")

    # опции маршрута тарифа "Свой"
    CAR_OPTION = (By.XPATH, ".//img[contains(@src, 'car.')]/..")
    WALK_OPTION = (By.XPATH, ".//img[contains(@src, 'walk')]/..")
    TAXI_OPTION = (By.XPATH, ".//img[contains(@src, 'taxi')]/..")
    BIKE_OPTION = (By.XPATH, ".//img[contains(@src, 'bike')]/..")
    SCOOTER_OPTION = (By.XPATH, ".//img[contains(@src, 'scooter')]/..")
    DRIVE_OPTION = (By.XPATH, ".//img[contains(@src, 'drive')]/..")

    # кнопка Вызвать такси
    BUTTON_CALL_TAXI = (By.XPATH, ".//div[@class = 'results-container']//button")

    # кнопка Забронировать
    BUTTON_BOOK_CAR = (By.XPATH, ".//button[@class='button round']")
