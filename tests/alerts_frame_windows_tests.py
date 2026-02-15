import time

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):  #  проверка открытия новой вкладки и текста на ней
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            test_result = new_tab_page.check_opened_new_tab()
            assert test_result == "This is a sample page", "Новая вкладка не открылась или не верный текст"

        def test_new_window(self, driver):  #  проверка открытия новой страницы
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            test_result = browser_window_page.check_opened_new_window()
            assert test_result == "This is a sample page", "Новая страница не открылась или не верный текст"


    class TestAlertsPage:

        def test_see_alert(self, driver):  #  проверка появления попапа
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()  #  метод появления попапа с вытягиванием текста на нем
            assert alert_text == 'You clicked a button'

        def test_alert_appear_5_sec(self, driver):  #  проверка появления попапа после 5 секунд
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()  #  метод появления попапа после 5 секунд с вытягиванием текста на нем
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_check_confirm_alert(self, driver):  #  проверка появления попапа и нажатия на кнопку в нем
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()  #  метод появления попапа нажатия кнопки и проверки текста
            assert alert_text == 'You selected Ok'

        def test_prompt_alert(self, driver):  #  проверка появления попапа, ввода в него текста и нажатия на кнопку в нем
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()  #  метод появления попапа, ввода в него текста нажатия кнопки и проверки текста
            assert alert_text == f'You entered {text}'  #  assert text in allert_text - второй вариант проверки
