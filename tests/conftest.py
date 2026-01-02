import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="function")  #  фикстура по запуску браузера, скоуп функ - драйвер открывается и закр для каждого теста
def driver():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)  #  открывается браузер хром, скачать надо библ webdriver-manager
    driver.maximize_window()  #  открывает браузер на весь экран
    yield driver  #  возвращает драйвер
    driver.quit()  #  закрывает браузер (тирдаун - действия после окончания тестов)