from AutomationPractice.Menus.headerPage import HeaderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime


class AuthenticationPage:
    page_subheading = "//h1[@class='page-subheading']"
    text_account_created_success = "Your account has been created."
    alert_success = "//p[contains(@class,'alert-success')]"
    my_acc_link_list = "//ul[contains(@class,'myaccount-link-list')]"
    link_my_personal_information = "//ul[contains(@class,'myaccount-link-list')]//a[@title='Information']"
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
    input_my_personal_first_name = "firstname"
    input_customer_last_name = "customer_lastname"
    input_my_personal_last_name = "lastname"
    input_customer_email = "email"
    input_customer_password = "passwd"
    select_day = "days"
    option_select_day = "//select[@id='days']/option[@value=dayVal]"
    option_selected_day = "//select[@id='days']//option[@selected='selected']"
    select_month = "months"
    option_select_month = "//select[@id='months']/option[@value=monthVal]"
    option_selected_month = "//select[@id='months']//option[@selected='selected']"
    select_year = "years"
    option_select_year = "//select[@id='years']/option[@value=yearVal]"
    option_selected_year = "//select[@id='years']//option[@selected='selected']"
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
        self.driver.find_element(By.ID, self.select_day).click()
        self.driver.find_element(By.XPATH, self.option_select_day.replace('dayVal', str(formattedDate.day))).click()
        self.driver.find_element(By.ID, self.select_month).click()
        self.driver.find_element(By.XPATH, self.option_select_month.replace('monthVal', str(formattedDate.month))).click()
        self.driver.find_element(By.ID, self.select_year).click()
        self.driver.find_element(By.XPATH, self.option_select_year.replace('yearVal', str(formattedDate.year))).click()

    def clickRegister(self):
        self.driver.find_element(By.ID, self.button_register).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.my_acc_link_list)))

    def validateSuccessBanner(self, text):
        if self.driver.find_element(By.XPATH, self.alert_success).text.strip() == text:
            assert True
        else:
            assert False

    def clickOnMyPersonalInformation(self):
        self.driver.find_element(By.XPATH, self.link_my_personal_information).click()

    def getFirstName(self):
        return self.driver.find_element(By.ID, self.input_my_personal_first_name).get_attribute('value').strip()

    def getLastName(self):
        return self.driver.find_element(By.ID, self.input_my_personal_last_name).get_attribute('value').strip()

    def getCustomerEmail(self):
        return self.driver.find_element(By.ID, self.input_customer_email).get_attribute('value').strip()
