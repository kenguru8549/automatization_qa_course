from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Вася')  #  проверяем видимость эл и с пом функции сенд кис заполнение поля FULL_NAME
        self.element_is_visible(self.locators.EMAIL).send_keys('dfg@dfg.ru')  # заполнение поля...
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('МО')  # заполнение поля...
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Реутов')  # заполнение поля...
        self.element_is_visible(self.locators.SUBMIT).click()  #  проверяем видимость кнопки и нажимаем на нее
