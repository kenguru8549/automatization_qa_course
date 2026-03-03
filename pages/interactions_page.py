import random

from  locators.interactions_page_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)  #  выбираем два случайных элемента
        item_what = item_list[0]  #  элемент откуда перемещаем
        item_where = item_list[1]  #  элемент куда перемещаем
        self.action_dgar_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        print(order_before)
        print(order_after)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)  #  выбираем два случайных элемента
        item_what = item_list[0]  #  элемент откуда перемещаем
        item_where = item_list[1]  #  элемент куда перемещаем
        self.action_dgar_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        print(order_before)
        print(order_after)
        return order_before, order_after