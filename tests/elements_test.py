import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:  #  создали класс для проверки страницы Test-box (раздел с регистрацией пользоватиеля)

        def test_test_box(self, driver):  #  функ по вводу данных и регистрации и проверки рег страницы тест-бокс
            test_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')   #  из класса бейспэйдж импортируем драйвер, открываем урл
            test_box_page.open()  #  открываем браузер из класса. там есть функция open
            full_name, email, current_address, permanent_address = test_box_page.fill_all_fields()  #  заполняем поля и жмем на кнопку сабмит из функ филолфилдс из класса текстбокспэйдж
            output_name, output_email, output_cur_addr, output_per_addr = test_box_page.check_filled_form()
            assert full_name == output_name, 'the full name does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert email == output_email, 'the email does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert current_address == output_cur_addr, 'the current address name does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки
            assert permanent_address == output_per_addr, 'the permanent address does not match'  #  проверка входных и выходных данных, через запятую написали текст ошибки, через запятую написали текст ошибки

    class TestCheckBox:  #  создали класс для проверки страницы Check-box (раздел с активацией и дезакт чекбоксов)
        def test_check_box(self, driver):  #  функ по актив и дезакт чекбоксов и проверки страницы чек-бокс
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')  # из класса чекбокспэйдж импортируем драйвер, открываем урл
            check_box_page.open()  # открываем браузер из класса, там есть функция open
            check_box_page.open_full_list()  #  открываем дерево чекбоксов
            check_box_page.click_random_checkbox()  #  проверяем все чекбоксы
            input_check_box = check_box_page.get_checked_checkboxes()  #  проверяем нажатые чекбоксы
            output_result = check_box_page.get_output_result()  #  проверяем названия нажатых чекбоксов
            assert input_check_box == output_result, 'чекбоксы и вывод чекбоксов не совпал'  #  проверяем совпадение нажатых и отображенных чекбоксов, пишем сообщение об ошибке если не совпадут

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver,'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'Значение "Yes" не совпадает'
            assert output_impressive == 'Impressive', 'Значение "Impressive" не совпадает'
            assert output_no == 'No', "Значение 'No' не совпадает"

    class TestWebTable:
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result


        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_people(key_word)
            table_result = web_table_page.chech_search_person()
            assert key_word in table_result, "Юзер не найден в таблице"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]  #  создаем нового юзера и берем фамилию с 1 индексом
            web_table_page.search_some_people(lastname)  #  ищем юзера по фамилии
            age = web_table_page.update_person_info()  #  обновили возраст юзера
            row = web_table_page.chech_search_person()  #  проверяем, что данные возраста изменились
            time.sleep(4)
            assert age in row, "карточка юзера не изменилась"


        def test_web_table_delete_person(self, driver):  #  тест удаления юзера
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]  # создаем нового юзера и берем имейл с 1 индексом
            web_table_page.search_some_people(email)  # ищем юзера по имейлу
            web_table_page.delete_person()  #  удаляем юзера
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):  #  тест на кол. строк в таблице
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()  #  метод подсчета строк
            assert count == [5, 10, 20, 25, 50, 100], "Номер не меняется или неправильное количество строк"  #  проверяем, что каунт равен массиву

    class TestButtonsPage:  #  класс страницы кнопки
        def test_different_click_on_the_buttons(self, driver):  #  функ. нажатия на все кнопки на странице
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', "Не нажата кнопка дабл"
            assert right == 'You have done a right click', "Не нажата кнопка ПКМ"
            assert click == 'You have done a dynamic click', "Не нажата кнопка ЛКМ"


    class TestLinksPage:  #  класс страницы ссылки

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            print(href_link, current_url)
            assert href_link == current_url, "ссылка сломана или не верный урл"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "ссылка сломана или не верный урл"

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open()
            file_name, result = upload_page.upload_file()
            assert file_name == result, "файл не скачался"

        def test_download_file(self, driver):
            download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open()
            check = download_page.download_file()
            assert check is True, "файл не закачался"

class TestDynamicPropertiesPage:


    def test_dynamic_properties(self, driver):  #  тест проверки смены цвета кнопки
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_before != color_after, "Цвет не поменялся"

    def test_appear_button(self, driver):  #  тест проверки появления кнопки
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_button()
        assert appear is True, "Кнопка не появилась после 5 секунд"

    def test_enable_button(self, driver):  #  тест проверки кликабельности кнопки, через 5 секунд
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, "Кнопка не кликабельна после 5 секунд"

