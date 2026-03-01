from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait  #  скачали библиотеку ожидания
from selenium.webdriver.support import expected_conditions as EC #  библ неявные ожидания элемента на стр


class BasePage:  #  создаем главный класс базовой страницы, другие бкдкт его наследовать
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):  #  открытие главной страницы
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):  #  метод видимость элемента на странице
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))  #  жди драйвер с таймаутом пока явное ожидание видимости эл локатор


    def elements_are_visible(self, locator, timeout=5):  #  метод видимость элемента на странице
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))  #  все элементы выдимы

    def element_is_present(self, locator, timeout=5):  #  метод видимость элемента на странице, ищет в дом дереве без скрола страницы
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):  #  все элементы выдимы
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):  #  метод не видимость элемента на странице
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):  #  метод кликабельность элемента на странице
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):  #  метод перемещения к элементу
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):  #  метод даблклика по элементу
        action = ActionChains(self.driver)  #  импортируем библиотеку ActionChains
        action.double_click(element)  #  делаем дабл клик на элемент
        action.perform()  #  команда для запуска двойного клика
    def action_right_click(self, element):
        action = ActionChains(self.driver)  # импортируем библиотеку ActionChains
        action.context_click(element)  # делаем клик правой кнопкой мыши на элемент
        action.perform()  # команда для запуска двойного клика

    def action_dgar_and_drop_by_offset(self, element, x_coords, y_coords):  #  метод перемещения по странице (делаем для слайдера)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)  #  зажмает точку на экране и двигает ее по координатам
        action.perform()  #  запускаем перемещение точки по координатам

    def action_move_to_element(self, element):  #  метод наведения мыши на элемент
        action = ActionChains(self.driver)
        action.move_to_element(element)  #  перемещаем мышь к элементу
        action.perform()  #  запускаем


