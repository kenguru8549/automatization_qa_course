import time

from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_test_box(self, driver):  #  открытие страницы в браузере
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')   #  из класса бейспэйдж импортируем драйвер, открываем урл
            test_box_page.open()  #  открываем браузер из класса. там есть функция open
            test_box_page.fill_all_fields()  #  заполняем поля и жмем на кнопку сабмит из функ филолфилдс из класса текстбокспэйдж
            output_name, output_email, output_cur_addr, output_per_addr = test_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)


