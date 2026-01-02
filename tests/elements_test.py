import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_test_box(self, driver):  #  открытие страницы в браузере
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/test-box')   #  из класса бейспэйдж импортируем драйвер, открываем урл
            test_box_page.open()  #  открываем браузер из класса. там есть функция open
            test_box_page.fill_all_fields()  #  заполняем поля и жмем на кнопку сабмит из функ филолфилдс из класса текстбокспэйдж
            time.sleep(5)


