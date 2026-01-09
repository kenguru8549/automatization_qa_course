from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())  #  next позволяет взять каждое значение по 1 разу (1 итерация)
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)  #  проверяем видимость эл и с пом функции сенд кис заполнение поля FULL_NAME
        self.element_is_visible(self.locators.EMAIL).send_keys(email)  # заполнение поля...
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)  # заполнение поля...
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)  # заполнение поля...
        self.element_is_visible(self.locators.SUBMIT).click()  #  проверяем видимость кнопки и нажимаем на нее
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[0] #  получаем текст методлом текст
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]  #  сплит создает лист с двумя значениями, [1] оставляет 2 значение
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]  #  text выводит текст по лакатору, который есть  в дереве дом
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
