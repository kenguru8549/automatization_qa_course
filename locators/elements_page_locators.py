from selenium.webdriver.common.by import By


class TextBoxPageLocators:

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


