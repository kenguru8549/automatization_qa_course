import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLokators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
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

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):  #  раскрытие дерева чекбоксов
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()  #  проверяем видимость кнопки + и нажимаем на нее

    def click_random_checkbox(self):  #  нажатие на рандомный чекбокс
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)  #  проверка видимости всех чекбоксов
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]  #  выбираем диапазон из списка, будет любой с методом рандом
            if count > 0:
                self.go_to_element(item)  #  добавляем поиск элемента
                item.click()  #  кликаем на элемент
                print(item.text)
                count -= 1  #  уменьшаем каунт на 1
            else:
                break

    def get_checked_checkboxes(self):  #  функ нажатия на чекбоксы
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)  #  элемент чекнут в дом дереве
        data = []
        for box in checked_list:  #  запускаем цикл просмотра просчелкнутых элементов
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)  #  оставшиеся просщелкнутые элементы
            data.append(title_item.text)  #  добавляем в список оставшиеся не чекнутые чекбоксы (текст)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()  #  привели к общему виду

    def get_output_result(self):  #  функ проверки результата нажатия на чекбоксы, текст с названиями нажатых чекбоксов
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)  # элемент чекнут в дом дереве
        data = []
        for item in result_list:  # запускаем цикл просмотра просчелкнутых элементов
            data.append(item.text)  # добавляем в список оставшиеся не чекнутые чекбоксы (текст)
        return str(data).replace(' ', '').lower()  #  привели к общему виду


class RadioButtonPage(BasePage):  #  создали новый класс и унаследовались от бейспэйдж
    locators = RadioButtonPageLocators()
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                  'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                  'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()  #  в функцию чоизес подставляется значение, например ес и его локатор и жмем нп него

    def get_output_result(self):  #  получаем значения результат нажатия радиобатона (текст)
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self):  #  создание нового юзера и добавление его в таблицу
        count = 1  #  создастся 1 юзер, цифру можно менять, во избежание пестицида
        while count != 0:
            person_info = next(generated_person())  #  некстом вытягиваем одну итерацию
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()  #  нажатие на кнопку для создания юзера
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()  # нажатие на кнопку подтверждение юзера
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):  #  проверка, что новый юзер добавился в таблицу
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_some_people(self, key_word):  #  поиск пользователя в таблице
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)  #  вставка пользователя в поле поиска

    def chech_search_person(self):  #  выбор найденного пользователя
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)  #  нашли кнопку корзины в строке
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARRENT)#  ищем родительский элемент в строке
        return row.text.splitlines()

    def update_person_info(self):  # редактирование пользователя
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()  # нажимаем на кнопку редактирования
        self.element_is_visible(self.locators.AGE_INPUT).clear()  # стираем возраст в поле эйдж
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)  # записываем возраст в поле эйдж
        self.element_is_visible(self.locators.SUBMIT).click()  # нажимаем кнопку сабмит
        return str(age)

    def delete_person(self):  #  создаем метод удаления юзера
        self.element_is_visible(self.locators.DELETE_BUTTON).click()  #  нажатие на кнопку удаления

    def check_deleted(self):  #  метод проверки видимости надписи о удаленном юзере
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text  #  видимость в дереве, возвращаем текст

    def select_up_to_some_rows(self):  #  метод проверки строк
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)  #  кнопка выпадшка с кол записей на странице
            self.go_to_element(count_row_button)  #  готуэлемент делает переход к элементу на странице, если он не видим
            count_row_button.click()  #  нажатие на кнопку выпадающего списка кол страниц
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()  #  подставляем в локатор Х из цикла, будет (5, 20 и т.д.)
            data.append(self.check_count_rows())  #  добавляем количество строк в список из метода ниже
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)  #  список количества людей в дом-дереве
        return len(list_rows)  #  возвращаем длину списка


class ButtonsPage(BasePage):  #  страница кнопок
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):  #  метод нажатия на кнопки
        if type_click == 'double':
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))  #  дабл клик на кнопку дабл клик
            return self.check_clicked_on_the_button(self.locators.SUCCES_DOUBLE)  #  возвращаем ответ
        if type_click == 'right':
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))    #  ПКМ на кнопку дабл клик
            return self.check_clicked_on_the_button(self.locators.SUCCES_RIGHT)  #  возвращаем ответ
        if type_click == 'click':
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()    #  ЛКМ на кнопку дабл клик
            return self.check_clicked_on_the_button(self.locators.SUCCES_CLICK_ME)  #  возвращаем ответ


    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text  #  возвращаем результат нажатия кнопки, кот. появится в дом дереве

class LinksPage(BasePage):
    locators = LinksPageLokators()

    def check_new_tab_simple_link(self):  #  проверка работы ссылок
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)  #  определяем ссылку на экране
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href, verify=False)  #  запрос ссылки
        if request.status_code == 200:
            simple_link.click()            #  жмем на ссылку
            self.driver.switch_to.window(self.driver.window_handles[1])  #  переключение на новую вкладку, хэндл отображает все вкладки, их будет 2, по индексу 1 (2я). Говорим драйверу - переключи свое внимание на окно с индексом 1
            url = self.driver.current_url  #  определяем отоборажаемую ссылку в новой вкладке
            return link_href, url
        else:
            return link_href, request.status_code

    def check_broken_link(self, url):  #  проверка сломаной ссылки
        request = requests.get(url, verify=False)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code

class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)  #  добавляем файл в инпут
        os.remove(path)  #  удаляет созданный файл
        text = self.element_is_present(self.locators.UPLOADED_RESULT).text  #  проверяем, что появился текст загруженного файла
        return file_name.split('\\')[-1], text.split('\\')[-1]  #  т.к. путь разный мы используем сплит для создания листа и определения последнего индекса

    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')  #  получение ссылки на картинку
        link_b = base64.b64decode(link)  #  декодируем ссылку на картинку в байты
        path_name_file = rf'C:\Users\guskov-av\PycharmProjects\automatization_qa_course\filetest{random.randint(0, 999)}.jpg'  #  создаем файл картинку
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')  #  находим значения в ссылке картинки закод-й в base64, b-байты и их значение, чтобы обрезать урл
            f.write(link_b[offset:])  #  записываем нужную чать урла без передней отсеченной части
            check_file = os.path.exists(path_name_file)  #  проверяем наличие созданного файла
            f.close()  #  закрываем файл
        os.remove(path_name_file)  #  удаляем файл
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()
    def check_changed_of_color(self):  #  метод определения цвета записи кнопки
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)  #  нашли кнопку
        color_button_before = color_button.value_of_css_property('color')  #  метод валью_... вытягивает цвет до изменений
        time.sleep(6)
        color_button_after = color_button.value_of_css_property('color')  # метод валью_... вытягивает цвет после изменений
        return color_button_before, color_button_after

    def check_appear_button(self):
        try:                        #  используется для обработки исключений, возникающих во время выполнения программы
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SECOND_BUTTON)  #  код, который может вызвать ошибку
        except TimeoutException:  #  приходит такая ошибка, обрабатываем ее
            return False
        return True

    def check_enable_button(self):  #  метод проверки кликабельности кнопки
        try:                        #  используется для обработки исключений, возникающих во время выполнения программы
            self.element_is_clickable(self.locators.ENABLE_BUTTON)  #  код, который может вызвать ошибку
        except TimeoutException:  #  приходит такая ошибка, обрабатываем ее
            return False
        return True
