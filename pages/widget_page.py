import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    ProgressBarPageLocators, SliderPageLocators, TabsPageLocators
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

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):  # метод установки даты
        date = next(generated_date())  # берем значения из функции генерации даты
        input_date = self.element_is_visible(self.locators.DATE_INPUT)  #  определяем поле ввода даты
        value_date_before = input_date.get_attribute('value')  #  определяем значение в поле даты
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')  #  определяем значение в поле даты после изменения даты
        return value_date_before, value_date_after

    def select_date_and_time(self):  # метод установки даты и времени
        date = next(generated_date())  # берем значения из функции генерации даты
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)  #  определяем поле ввода даты
        value_date_before = input_date.get_attribute('value')  #  определяем значение в поле даты
        input_date.click()
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()  #  кликаем на месяц
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)  #  выбираем месяц из списка
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()  # кликаем на год
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')  # указываем год из списка
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)  # выбираем месяц из списка
        input_date_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)  # определяем поле ввода даты
        value_date_after = input_date.get_attribute('value')  # определяем значение в поле даты после изменения даты
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):  #  метод для выбора месяца и года
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):  #  метод выбора дня из списка
        item_list = self.elements_are_present(elements)  #  список дней
        for item in item_list:  #  проходимся по спику
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):  #  метод проверки слайдера
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')  #  определяем значение слайдера до изменения
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)  #  нашли слайдер
        self.action_dgar_and_drop_by_offset(slider_input, random.randint(1, 100), 0)  #  двигаем по оси икс в рандомном значении
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')  # определяем значение слайдера после изменения
        return value_before, value_after  #  возвращаем значение из поля

class ProgressBarPage(BasePage):  #  метод проверки прогресс бара
    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text  #  значение до изменения прог.бара
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)  #  нашли кнопку
        progress_bar_button.click()  #  первое нажатие на кнопку
        time.sleep(random.randint(2, 5))  #  рандомная задержка по времени
        progress_bar_button.click()  # повторное нажатие на кнопку
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                    'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                    'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return [button.text, len(what_content)]

