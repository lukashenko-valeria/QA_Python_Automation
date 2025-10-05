from selenium.webdriver.common.by import By

class CardPageLocators:
    BUTTON_ADD = (By.XPATH, ".//*[text()=' Добавить в покупки']")
    RECIPE_NAME_H1 = (By.TAG_NAME, 'h1')
