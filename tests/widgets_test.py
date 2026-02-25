import time

from pages.widget_page import AccordianPage, AutoCompletePage, DatePickerPage


class TestWidgets:

    class TestAccordianPage:

        def test_accordian(self, driver):  #  проверка работы аккордиона
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')  #  первый разворот
            second_title, second_content = accordian_page.check_accordian('second')  #  второй разворот
            third_title, third_content = accordian_page.check_accordian('third')  #  третий разворот
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0 #  проверяем текст заголовка и что текст больше 0 символов
            assert second_title == 'Where does it come from?' and second_content > 0  # проверяем текст заголовка и что текст больше 0 символов
            assert third_title == 'Why do we use it?' and third_content > 0  # проверяем текст заголовка и что текст больше 0 символов

    class TestAutoCompletePage:
        def test_fill_multi_autocomplete(self, driver):  #  проверка добавления нескольких значений в поле фильтра
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()  #  добавление цветов в фильтр
            colors_result = autocomplete_page.check_color_in_multi()  #  проверка добавленных цветов в фильтр
            assert colors == colors_result

        def test_remove_value_from_multi(self, driver):  #  проверка добавления и удаления нескольких значений в поле фильтра
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_autocomplete(self, driver):  #  проверка добавления одного значений в поле фильтра
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result

    class TestDatePickerPage:

        def test_change_date(self, driver):  #  проверка добавления и удаления нескольких значений в поле фильтра
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        def test_change_date_and_time(self, driver):  #  проверка добавления и удаления нескольких значений в поле фильтра
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            assert value_date_before != value_date_after

