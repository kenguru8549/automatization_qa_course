import random

from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':   #  создаем словарь
                         {'title': self.locators.SECTION_FIRST,
                          'content': self.locators.SECTION_CONTENT_FIRST},
                     'second':
                         {'title': self.locators.SECTION_SECOND,
                          'content': self.locators.SECTION_CONTENT_SECOND},
                     'third':
                         {'title': self.locators.SECTION_THIRD,
                          'content': self.locators.SECTION_CONTENT_THIRD}
                     }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:  #  делаем обработку при первом аккордионе клик не нужен, обработает ошибку и соберет текст
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, section_content]

class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):  #  метод добавления нескольких значений в поле фильтра
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))  #  создали дата класс и генератор колор для выбора цвета, k - колич. добавленных значений
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)  # находим поле фильтра
            input_multi.send_keys(color)  # заполняем значением цвета из списка цветов
            input_multi.send_keys(Keys.ENTER)  # нажимаем на энтер
        return colors
    def remove_value_from_multi(self):  #  метод удаления нескольких значений в поле фильтра
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))  #  количество записей в фильтре до
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)  #  количество записей в фильтре после добавления значений
        for value in remove_button_list:  #  удаление всех значений
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))  #  количество записей в фильтре после
        return count_value_before, count_value_after

    def check_color_in_multi(self):  #  метод сверки цветов
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)  #  список цветов
        colors = []
        for color in color_list:  #  добавляем все цвета в список колорс
            colors.append(color.text)
        return colors

    def fill_input_single(self):  #  метод добавления одного значений в поле фильтра
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):  #  метод сверки цвета
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


