import time

from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            person_info = form_page.fill_form_fields()  #  данные вносимые в форму при создании юзера
            result = form_page.form_result()  #  данные в форме созданного юзера
            assert [person_info.firstname + " " + person_info.lastname, person_info.email] == [result[0], result[1]], "данные не совпадают"  #  резалт идет как картеж(тапл) берем индексы, а персон как список, берем имена