import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AutomationPractice.Menus.AuthenticationPage import AuthenticationPage

baseURL = "http://www.automationpractice.pl/index.php"

FEATURE_FILE = '../Features/AuthenticationPage.feature'

scenarios(FEATURE_FILE)

browser = webdriver.Chrome()
Authentication = AuthenticationPage(browser)


@given("I open website")
def open_website():
    browser.get(baseURL)
    browser.maximize_window()


@given("I navigate to login page")
def navigate_to_login_page():
    Authentication.clickSignUp()


@when(parsers.parse('I fill my personal information:\n{personal_info_table}'))
def fill_personal_information(personal_info_table):
    parsedPersonalInfo = parse_str_table(personal_info_table)
    Authentication.setTitle(parsedPersonalInfo['Title'])
    Authentication.setFirstName(parsedPersonalInfo['FirstName'])
    Authentication.setLastName(parsedPersonalInfo['LastName'])
    Authentication.setPersonalInformationPassword(parsedPersonalInfo['Password'])
    Authentication.setDateOfBirth(parsedPersonalInfo['DateOfBirth'])
    time.sleep(5)


@when(parsers.cfparse("I enter email {email}"))
def enter_email(email):
    Authentication.setCreateEmail(email)

@then("I am redirected to create an account page")
def validate_create_account_page():
    Authentication.validatePageHeading(Authentication.heading_create_account)

@when("I click register")
def click_register():
    Authentication.clickRegister()
@then("Then I am redirected to my account screen")
def validate_my_account_page():
    Authentication.validatePageHeading(Authentication.heading_create_account)

@when("I click on create account button")
def click_create_account_button():
    Authentication.clickCreateAccout()

def parse_str_table(table_with_headers):
    list_table_rows = table_with_headers.split("\n")
    list_headers = str(list_table_rows[0]).strip("|").split("|")
    dict_table = {}
    for header in list_headers:
        header_text = header.strip()
        lst_row = None
        for i in range(1, list_table_rows.__len__()):
            list_temp = list_table_rows[i].strip("|").split("|")
            lst_row = list_temp[list_headers.index(header)].strip()

        dict_table[header_text] = lst_row

    return dict_table
