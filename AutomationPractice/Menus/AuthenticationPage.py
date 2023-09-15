from selenium import webdriver
from AutomationPractice.Menus.headerPage import HeaderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class AuthenticationPage:
    heading_create_account = "CREATE AN ACCOUNT"
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

    def validatePageHeading(self, heading):
        if self.driver.find_element(By.XPATH, self.txt_page_heading_xpath).text.strip() == heading:
            assert True
        else:
            assert False
