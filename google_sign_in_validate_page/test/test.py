from selenium import webdriver
from google_sign_in_validate_page.pages.sign_in_page import SignIn
from google_sign_in_validate_page.pages.create_account_page import CreateAccount
import time

driver = webdriver.Chrome("D:/py/chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://accounts.google.com")


# variables
validation_error = "Имя пользователя может включать латинские буквы (a-z), цифры (0-9) и точку (.)."
email_list = {'@a.a', 'a@-a.a', 'a@a@a.a', 'a@a'}
user_dictionary = {'fn':'Yevhen', 'ln':'Prodchenko', 'password': 'Abc123456!'}

SignIn(driver).create_account()
SignIn(driver).create_account_for_you()

