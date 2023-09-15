class ContactUsPage:
    txt_page_heading_xpath = "//h1[contains(@class,'page-heading')]"
    select_subject_heading = "id_contact"
    input_email = "email"
    input_order_reference = "id_order"
    input_message = "message"
    button_send = "submitMessage"

    alert_general_xpath = "//div[contains(@class, 'alert-danger')]"

    alert_success_general_xpath = "//p[contains(@class, 'alert-success')]"
