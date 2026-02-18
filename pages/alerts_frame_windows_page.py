import random
import time

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):  #  метод открытия новой вкладки
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()  #  кликаем по кнопке открытия новой вкладки
        self.driver.switch_to.window(self.driver.window_handles[1])  #  переключаемся на открывшуюся вкладку с индексом 1
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):  #  метод открытия новой страницы
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()  #  кликаем по кнопке открытия новой вкладки
        self.driver.switch_to.window(self.driver.window_handles[1])  #  переключаемся на открывшуюся вкладку с индексом 1
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):  #  метод появления попапа
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()  #  нажимаем на кнопку для появления попапа
        alert_window = self.driver.switch_to.alert  #  переключаемся на появившийся попап
        return alert_window.text  #  возвращаем текст из попапа

    def check_alert_appear_5_sec(self):  #  метод появления попапа
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()  #  нажимаем на кнопку для появления попапа
        time.sleep(6)
        try:  #  добавили обработку ошибки, чтобы кейс проходил
            alert_window = self.driver.switch_to.alert
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.driver.switch_to.alert
            return alert_window.text

    def check_confirm_alert(self):  #  метод появления попапа, нажатия на нем кнопки и проверки текста на осн. стр. после нажатия
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()  # нажимаем на кнопку для появления попапа
        alert_window = self.driver.switch_to.alert  # переключаемся на появившийся попап
        alert_window.accept()  #  нажимаем на ок в появившемся попапе, если нажать отмена, то будет метод дисмисс
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text  #  текст, который появится на осн. странице, после нажатия кнопки на попапе
        return text_result

    def check_prompt_alert(self):  #  метод появления попапа, написания в нем текста и проверки написанного
        text = f'autotest{random.randint(0, 999)}'  #  текст, который будем записывать в попапе
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()  # нажимаем на кнопку для появления попапа
        alert_window = self.driver.switch_to.alert  # переключаемся на появившийся попап
        alert_window.send_keys(text)  #  заполняем строку текстом
        alert_window.accept()  #  нажимаем на ок в появившемся попапе, если нажать отмена, то будет метод дисмисс
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text  #  текст, который появится на осн. странице, после нажатия кнопки на попапе
        return text, text_result  #  возвращаем написанный текст и текст после нажатия кнопки

class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):  #  метод нахождения фреймов на странице
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')  #  определяем ширину фрейма
            height = frame.get_attribute('height')  #  определяем высоту фрейма
            self.driver.switch_to.frame(frame)  #  переключаемся на сам фрейм через его локатор
            text = self.element_is_present(self.locators.TITLE_FRAME).text  #  вытягиваем текст фрейма
            self.driver.switch_to.default_content()  #  возвращаемся из фрейма на основную страницу
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')  #  определяем ширину фрейма
            height = frame.get_attribute('height')  #  определяем высоту фрейма
            self.driver.switch_to.frame(frame)  #  переключаемся на сам фрейм через его локатор
            text = self.element_is_present(self.locators.TITLE_FRAME).text  #  вытягиваем текст фрейма
            self.driver.switch_to.default_content()  # возвращаемся из фрейма на основную страницу
            return [text, width, height]

class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    def check_nested_frame(self):  #  метод нахождения вложенных фреймов на странице
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)  #  находим родительский фрейм
        self.driver.switch_to.frame(parent_frame)  #  переключаемся на фрейм
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text  #  берем из фрейма текст
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)  #  находим детский фрейм
        self.driver.switch_to.frame(child_frame)  #  переключаемся на фрейм
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text  #  берем из фрейма текст
        return parent_text, child_text

class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    def check_modal_dialogs(self):  #  метод нахождения модального окна
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()  #  кликаем на кнопку открытия малого модального окна
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text  #  берем текст заголовка модального окна
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text  # берем текст тела модального окна
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()  # кликаем на кнопку закрытия модального окна
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()  # кликаем на кнопку открытия большого модального окна
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text  # берем текст заголовка модального окна
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text  # берем текст тела модального окна
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]