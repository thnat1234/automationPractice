from selenium.webdriver.common.by import By


class HeaderPage:
    link_contact_us = "contact-link"
    link_sign_in_xpath = "//a[contains(@class, 'login')]"
    link_signed_in_user_name_xpath = "//a[contains(@class, 'account')]"
    link_signed_in_user_logout = "//a[contains(@class, 'logout')]"
    href_header_logo = "header_logo"

    input_search = "search_query_top"
    button_submit_search = "//button[@name='submit_search']"

    link_cart_xpath = "//div[@class='shopping_cart']/a"
    link_cart_count = "//div[@class='shopping_cart']//span[@class='ajax_cart_quantity']"
    button_cart_checkout = "button_order_cart"

    # Menu
    link_main_women_xpath = "//a[contains(@title,'Women')]"
    link_main_dresses_xpath = "//a[contains(@title,'Dresses')]"
    link_main_tshirts_xpath = "//a[contains(@title,'T-shirts')]"
    link_main_blog_xpath = "//a[contains(@title,'Blog')]"

    # Try to shorten the xpath
    # Submenu
    link_submenu_tops_xpath = "//ul[contains(@class,'submenu-container')]//a[contains(@title,'Tops')]"
    link_submenu_tshirts_xpath = "//ul[contains(@class,'submenu-container')]//a[contains(@title,'T-shirts')]"
    link_submenu_blouses_xpath = "//ul[contains(@class,'submenu-container')]//a[contains(@title,'Blouses')]"

    def __init__(self, driver):
        self.driver = driver

    def clickSignUp(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.link_sign_in_xpath).click()
        self.driver.implicitly_wait(10)
