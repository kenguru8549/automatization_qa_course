from pages.widget_page import AccordianPage


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
