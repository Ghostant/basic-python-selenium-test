from selenium import webdriver
from google_sign_in_validate_page.pages.sign_in_page import SignIn
from google_sign_in_validate_page.pages.create_account_page import CreateAccount
import time


driver = webdriver.Chrome("D:/py/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://accounts.google.com")


# variables
validation_error = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
user_dictionary = {'fn': 'Yevhen', 'ln': 'Prodchenko', 'password': 'Abc123456!'}
sign_in_page = SignIn(driver)
create_account_page = CreateAccount(driver)


sign_in_page.create_account()
time.sleep(1)
sign_in_page.create_account_for_you()

time.sleep(1)
create_account_page.enter_firstname(user_dictionary['fn'])
create_account_page.enter_lastname(user_dictionary['ln'])
create_account_page.enter_password(user_dictionary['password'])
create_account_page.enter_confirmpassword(user_dictionary['password'])


for element in email_list:
    create_account_page.enter_username(element)
    create_account_page.click_next()
    time.sleep(1)
    assert validation_error in driver.page_source
