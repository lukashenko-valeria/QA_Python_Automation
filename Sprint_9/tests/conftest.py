import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import allure

REMOTE_DRIVER = True   # признак использования удаленного WebDriver из Селеноида при запуске в docker-контейнере


@pytest.fixture
@allure.title("Подключаем удаленный или локальный драйвер в зависимости от флага REMOTE_DRIVER")
def driver():
    if REMOTE_DRIVER:
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "114.0")
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": False
        })

        driver = webdriver.Remote(
            command_executor='http://selenoid:4444/wd/hub',
            options=options
        )
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    yield driver
    driver.quit()
