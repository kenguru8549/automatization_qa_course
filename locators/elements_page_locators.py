from selenium.webdriver.common.by import By


class TextBoxPageLocators:  #  класс для локаторов страницы TextBox
    #  form fields

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")  #  локатор поля Full Name
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")  #  локатор поля Email
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")  #  локатор поля Current Address
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")  #  локатор поля Permonent Address
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")  #  локатор кнопки Submit

    #created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")  #  локатор созданного поля Full Name решетка заменяет id там общее id output и частное name
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")  #  локатор поля Email
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")  #  локатор поля Email
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")  #  локатор поля Email

class CheckBoxPageLocators:  #  класс для локаторов страницы CheckBox

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")  #  локатор кнопки +
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")  #  локатор для 17 элементов, будет работа с циклом для поиска нужного
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")  #  чекбокс на который нажали
    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")  #  икспас локатор элемента для нахождения текста
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")  #  список вывода нажатых чекбоксов

class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:
    #  add person forms
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LASTNAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    #  tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARRENT = (".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    #  update
    UPDATE_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

class ButtonsPageLocators:

    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    #  result
    SUCCES_DOUBLE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    SUCCES_RIGHT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCES_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LinksPageLokators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")

    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")

class DynamicPropertiesPageLocators:
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id='enableAfter']")
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SECOND_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")