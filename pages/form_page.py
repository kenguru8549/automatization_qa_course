import os

from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())  #  добавлем юзера
        file_name, path = generated_file()  #  имя файла и путь, т.к. из генератед_файл возвращаем именно их
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)  #  заполняем поле ферстнэйм с помощью локатора и генератора имени
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)  #  добавляем фамилию
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)  #  добавляем имейл
        self.element_is_visible(self.locators.GENDER).click()  #  кликаем на пол
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)  #  добавляем сотовый
        self.element_is_visible(self.locators.SUBJECT).send_keys('Maths')  #  добавляем значение математика и оно остается не выбранным в строке
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)  #  нажимаем на энтэр, чтобы значение добавилось в строку сабджект
        self.element_is_visible(self.locators.HOBBIES).click()  #  кликаем на хобби
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)  #  добавляем файл, проставляя его путь к файлу
        os.remove(path)  #  удаляем созданный файл, чтобы не захломлять репозиторий
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)  #  заполняем адрес
        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))  #  перейти к невидимому элементу на экране, перекручивает экран
        self.element_is_visible(self.locators.SELECT_STATE).click()  #  кликаем на штат
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)  #  нажимаем на энтэр, чтобы значение добавилось
        self.element_is_visible(self.locators.SELECT_CITY).click()  # кликаем на город
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT).click()  #  нажимаем на кнопку сабмит
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)  #  список элементов нового юзера
        data = []
        for i in result_list:  #  проходим по каждому элементу и кладем в дату список всех элементов
            self.go_to_element(i)  #  переход к элементу
            data.append(i.text)  #  добавляем в список
        return data
