from selenium.webdriver.common.by import By


class OrderLocators:
    # Страница "Для кого самокат"
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STATION_SELECTION = (By.XPATH, ".//li[@class='select-search__row']")
    STATION_SELECTED = (By.XPATH, "//button[@value='1']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    # Страница "Про аренду"
    DATE_SELECTED = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    SELECT_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-arrow")
    COLOR_OF_SCOOTER_GREY = (By.ID, "grey")
    COLOR_OF_SCOOTER_BLACK = (By.ID, "black")
    COMMENT_BY_COURIER = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    LOWER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    BUTTON_YES = (By.XPATH, "//button[text()='Да']")
    ORDER_STATUS = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    ORDER_CHECK = (By.XPATH, "//div[@class='Input_InputContainer__3NykH']")

    TITLE_ORDER = (By.XPATH, "//div[@class='Order_Header__BZXOb'and text()='Для кого самокат']")
