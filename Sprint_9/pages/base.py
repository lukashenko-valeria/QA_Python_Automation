from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import allure

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

    @allure.step('Кликаем на элемент')
    def click_on_element(self, locator, timeout=30):
        try:
            elem = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            elem.click()
        except ElementClickInterceptedException:   # Если клик перехвачен, используем JavaScript
            elem = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", elem)

    @allure.step('Ищем элемент с ожиданием его появления в DOM страницы')
    def wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        return self.find_element_with_visibility_wait(locator).text

    @allure.step('Ищем по локатору поле ввода и отправляем в него текст')
    def input_text(self, locator, text):
        element = self.find_element_with_visibility_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текущий url сайта")
    def get_page_url(self):
        return self.driver.current_url

    @allure.title("Скроллим  вниз страницы")
    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.title("Скроллим к элементу")
    def scroll_to_element(self, locator):
        """Скроллит страницу к указанному элементу"""
        element = self.find_element_with_visibility_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)

    @allure.title("Находим скрытый элемент")
    def find_hidden(self, locator):
        return self.driver.find_element(*locator)

    @allure.title("Загружаем картинку")
    def load_picture(self, locator, picture_path):
        self.find_hidden(locator).send_keys(picture_path)

    @allure.step('Ожидаем, что URL содержит определенную часть')
    def wait_for_url(self, expected_url_part, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(expected_url_part)
        )

    @allure.step('Ожидаем, что элемент содержит определенный текст')
    def wait_for_text_in_element(self, locator, expected_text, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, expected_text)
        )

    @allure.step('Ожидаем исчезновение элемента')
    def wait_for_element_to_disappear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Ожидаем появление списка опций')
    def wait_for_options_to_appear(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(*locator)) > 0
        )

    @allure.step('Очищаем поле ввода')
    def clear_field(self, locator):
        element = self.find_element_with_visibility_wait(locator)
        element.clear()
