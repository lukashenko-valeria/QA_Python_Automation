from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    @allure.title('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открываем заданную страницу по URL с ожиданием ее загрузки')
    def open_page(self, url):
        self.driver.get(url)
        return self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step('Ищем элемент c ожиданием его видимости')
    def find_element_with_visibility_wait(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ищем элемент с ожиданием его кликабельности')
    def find_element_with_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator, timeout=30):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            elem.click()
        except ElementClickInterceptedException:  # Если клик перехвачен, используем JavaScript
            elem = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", elem)

    @staticmethod
    def click_on_element_without_locator(element):
        element.click()

    @allure.step('Получаем список элементов')
    def get_list_of_elements(self, locator):
        self.find_element_with_clickable(locator)
        list_of_elements = self.driver.find_elements(*locator)
        return list_of_elements

    @allure.step('Получаем текст элемента по локатору')
    def get_text_by_locator(self, locator):
        return self.find_element_with_visibility_wait(locator).text

    @allure.step('Получаем текст элемента по WEB-элементу или локатору')
    def get_text(self, element=None, locator=None):
        if element:
            return element.text  # если передали элемент, берем текст напрямую
        elif locator:
            return self.find_element_with_visibility_wait(locator).text
        else:
            raise ValueError("Must provide either element or locator")

    @allure.step('Ищем по локатору поле ввода и вводим в него текст')
    def input_text(self, locator, text):
        element = self.find_element_with_visibility_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Ожидаем исчезновение элемента')
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Наводим фокус на элемент i')
    def focus_on_element(self, locator):
        element = self.find_element_with_visibility_wait(locator)
        action = ActionChains(self.driver).move_to_element(element)
        action.perform()

    @allure.step('Проверяет, что элемент видимый')
    def element_is_visible(self, locator, timeout=10):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    @allure.step('Пролистываем блок до конца списка')
    def move_down_in_container(self, container_locator):
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container_locator)

    @allure.step('Ждем пока в элементе появится текст')
    def wait_text_is_visible(self, locator, text_to_be_visible):
        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element(locator, text_to_be_visible))

    @allure.step('Ждем пока изменится текст элемента')
    def wait_change_of_element(self, locator, text_to_be_changed):
        self.find_element_with_visibility_wait(locator)
        WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, str(text_to_be_changed)))
