from selenium import webdriver
from AutomationPractice.Menus.headerPage import HeaderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.common.exceptions import TimeoutException


class AuthenticationPage:
    heading_create_account = "CREATE AN ACCOUNT"
    heading_my_account = "MY ACCOUNT"
    txt_page_heading_xpath = "//h1[contains(@class,'page-heading')]"
    frm_create_account = "create-account_form"
    input_create_email = "email_create"
    button_create_account = "SubmitCreate"
    alert_create_account = "create_account_error"

    frm_login_id = "login_form"
    input_login_email = "email"
    input_login_password = "passwd"
    button_login = "SubmitLogin"
    link_forgot_password_xpath = "//p[contains(@class, 'lost_password')]/a"

    # Personal information
    rb_title_mr = "id_gender1"
    rb_title_mrs = "id_gender2"
    input_customer_first_name = "customer_firstname"
    input_customer_last_name = "customer_lastname"
    input_customer_email = "email"
    input_customer_password = "passwd"
    select_day = "days"
    select_month = "months"
    select_year = "years"
    button_register = "submitAccount"
    form_account_create = "account-creation_form"

    # There are two elements that can be found on the page, make sure that it is the one that is active or displayed
    alert_general_xpath = "//div[contains(@class, 'alert-danger')]"

    def __init__(self, driver):
        self.driver = driver
        self.HeaderPage = HeaderPage(self.driver)

    def setCreateEmail(self, email):
        self.driver.find_element(By.ID, self.input_create_email).clear()
        self.driver.find_element(By.ID, self.input_create_email).send_keys(email)

    def clickSignUp(self):
        self.HeaderPage.clickSignUp()

    def clickCreateAccout(self):
        self.driver.find_element(By.ID, self.button_create_account).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.form_account_create)))

    def validatePageHeading(self, heading):
        print("header is ")
        print(self.driver.find_element(By.XPATH, self.txt_page_heading_xpath).text.strip())
        if self.driver.find_element(By.XPATH, self.txt_page_heading_xpath).text.strip() == heading:
            assert True
        else:
            assert False

    def setFirstName(self, firstName):
        self.driver.find_element(By.ID, self.input_customer_first_name).clear()
        self.driver.find_element(By.ID, self.input_customer_first_name).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element(By.ID, self.input_customer_last_name).clear()
        self.driver.find_element(By.ID, self.input_customer_last_name).send_keys(lastName)

    def setPersonalInformationEmail(self, email):
        self.driver.find_element(By.ID, self.input_customer_email).clear()
        self.driver.find_element(By.ID, self.input_customer_email).send_keys(email)

    def setPersonalInformationPassword(self, passwd):
        self.driver.find_element(By.ID, self.input_customer_password).clear()
        self.driver.find_element(By.ID, self.input_customer_password).send_keys(passwd)

    def setTitle(self, title):
        if title == "Mr.":
            self.driver.find_element(By.ID, self.rb_title_mr).click()
        elif title == "Mrs.":
            self.driver.find_element(By.ID, self.rb_title_mrs).click()

    def setDateOfBirth(self, date):
        formattedDate = datetime.strptime(date, '%d/%m/%Y')
        print(formattedDate.date())
        print(formattedDate.day)
        print(formattedDate.month)
        print(formattedDate.year)
        dayselect = Select(self.driver.find_element(By.ID(self.select_day)))
        dayselect.select_by_index(3)
        time.sleep(5)
        #Select(self.driver.find_element(By.ID(self.select_month))).select_by_index(formattedDate.month)
        #Select(self.driver.find_element(By.ID(self.select_year))).select_by_value(str(formattedDate.year))

    def clickRegister(self):
        self.driver.find_element(By.ID, self.button_register).click()
        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.form_account_create)))

