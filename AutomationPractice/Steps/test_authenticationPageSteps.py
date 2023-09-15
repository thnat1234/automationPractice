import time
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
import pytest
from AutomationPractice.Menus.AuthenticationPage import AuthenticationPage

baseURL = "http://www.automationpractice.pl/index.php"

FEATURE_FILE = '../Features/AuthenticationPage.feature'

scenarios(FEATURE_FILE)

browser = webdriver.Chrome()
Authentication = AuthenticationPage(browser)


@given("I open website")
def open_website():
    browser.get(baseURL)


@given("I navigate to login page")
def navigate_to_login_page():
    Authentication.clickSignUp()


@when(parsers.parse('I fill my personal information:\n{personal_info_table}'))
def fill_personal_information(personal_info_table):
    jsonData = parse_str_table(personal_info_table)
    print(jsonData['DateOfBirth'])


@when(parsers.cfparse("I enter email {email}"))
def enter_email(email):
    Authentication.setCreateEmail(email)
    time.sleep(5)

@then("I am redirected to create an account page")
def validate_account_page():
    Authentication.validatePageHeading(Authentication.heading_create_account)


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
