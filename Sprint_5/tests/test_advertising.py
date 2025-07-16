from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators, AdvertLocators
import consts
import urls

class TestAdvertisementPlacement:

    def test_create_message_by_unauthorized_user(self, driver):
        driver.get(urls.MAIN_PAGE_URL)

        driver.find_element(*AdvertLocators.CREATE_AD_BTN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.TXT_ERROR))
        assert driver.find_element(*AdvertLocators.TXT_ERROR)

    def test_create_message_by_authorized_user(self, driver, ad_user):
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(AdvertLocators.CREATE_AD_BTN))
        driver.find_element(*AdvertLocators.CREATE_AD_BTN).click()  # Найти кнопку "Разместить объявление" и кликнуть на нее

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(AdvertLocators.NEW_AD_HEADER))  # Проверка формы создания объявления

        name_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.AD_NAME_INPUT))
        name_input.send_keys(consts.ADVERTISEMENT_NAME)   # Заполняем название товара

        category_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.CATEGORY_DROPDOWN))
        category_dropdown.click()   # Выбираем категорию товара

        books_category = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.BOOKS_CATEGORY))
        books_category.click()

        used_condition = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.USED_CONDITION))
        used_condition.click()    # Выбираем состояние товара

        city_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.CITY_DROPDOWN))
        city_dropdown.click()

        spb_city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.SPB_CITY))
        spb_city.click()    # Выбираем город

        description_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.DESCRIPTION_INPUT))
        description_input.send_keys(consts.ADVERTISEMENT_DESCRIPTION)   # Заполняем описание товара

        price_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.PRICE_INPUT))
        price_input.send_keys(consts.ADVERTISEMENT_PRICE)   # Указываем цену товара

        publish_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AdvertLocators.PUBLISH_BTN))
        publish_btn.click()   # Публикация объявления

        driver.get(urls.PROFILE_PAGE_URL)   # Переход на страницу профиля
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.UPLOADED_IMAGE))

        published_ad = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AdvertLocators.PUBLISHED_AD))
        assert consts.ADVERTISEMENT_NAME in published_ad.text
