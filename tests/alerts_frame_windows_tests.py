import time

from pages.alerts_frame_windows_page import BrowserWindowsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open()
            test_result = new_tab_page.check_opened_new_tab()
            assert test_result == "This is a sample page", "Новая вкладка не открылась или не верный текст"

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            test_result = browser_window_page.check_opened_new_window()
            assert test_result == "This is a sample page", "Новая страница не открылась или не верный текст"