from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()  #  кликаем по кнопке открытия новой вкладки
        self.driver.switch_to.window(self.driver.window_handles[1])  #  переключаемся на открывшуюся вкладку с индексом 1
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()  #  кликаем по кнопке открытия новой вкладки
        self.driver.switch_to.window(self.driver.window_handles[1])  #  переключаемся на открывшуюся вкладку с индексом 1
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title




