from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).fill('Вася')  #  проверяем видимость эл и с пом функции сенд кис заполнение поля FULL_NAME
        self.element_is_visible(self.locators.EMAIL).send_keys('dfg@dfg.ru')  # заполнение поля...
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('МО')  # заполнение поля...
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Реутов')  # заполнение поля...
        self.element_is_visible(self.locators.SUBMIT).click()  #  проверяем видимость кнопки и нажимаем на нее


    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text  #  получаем текст методлом текст
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address
