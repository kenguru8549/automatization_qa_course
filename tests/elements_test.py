import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_test_box(self, driver):  #  открытие страницы в браузере
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')   #  из класса бейспэйдж импортируем драйвер, открываем урл
            test_box_page.open()  #  открываем браузер из класса. там есть функция open
            full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()  #  заполняем поля и жмем на кнопку сабмит из функ филолфилдс из класса текстбокспэйдж
            output_name, output_email, output_cur_addr, output_per_addr = test_box_page.check_filled_form()
            assert full_name == output_name, 'the full name does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert email == output_email, 'the email does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert current_address == output_cur_addr, 'the current address name does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert permanent_address == output_per_addr, 'the permanent address does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки, через запятую написали текст ошибки


