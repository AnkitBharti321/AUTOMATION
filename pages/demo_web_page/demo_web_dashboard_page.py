from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage



class DemoWebDashboardPage(BasePage):
    # region Locators
    FIRST_NAME_FIELD = By.ID, "FirstName"
    LAST_NAME_FIELD = By.ID, "LastName"
    EMAIL_FIELD = By.ID, "Email"
    PASSWORD_FIELD = By.ID, "Password"
    CONFIRM_PASSWORD_FIELD = By.ID, "ConfirmPassword"
    REGISTER_BUTTON = By.ID, "register-button"
    LOGIN_BUTTON = By.XPATH, "//input[@value='Log in']"

    # endregion Locators
    #saucedemo Login


    # page class constructor
    def __init__(self, driver, title="Demo Web Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['demo_web_shop']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    # UI Automation

    # Amazon

    def register_account_to_demo_web_dashboard_page(self, value, gender, first_name, last_name, email, password):
        self.click_header_options(options=value)
        self.checkbox_by_label(how='xpath', label_path=f'//input[@id="gender-{gender}"]//following-sibling::label', checkbox_path=f'//input[@id="gender-{gender}"]')
        self.fill_out_text_field(by_locator=self.FIRST_NAME_FIELD, value=first_name)
        self.fill_out_text_field(by_locator=self.LAST_NAME_FIELD, value=last_name)
        self.fill_out_text_field(by_locator=self.EMAIL_FIELD, value=email)
        self.fill_out_text_field(by_locator=self.PASSWORD_FIELD, value=password)
        self.fill_out_text_field(by_locator=self.CONFIRM_PASSWORD_FIELD, value=password)
        self.click_element(by_locator=self.REGISTER_BUTTON)

    def get_complete_registration_confimation_message(self):
        return self.get_element_text(how='xpath', path="//div[@class='result']")

    def click_continue_button(self):
        self.click_element(how='xpath', path="//input[@value='Continue']")

    def get_logged_user_account_details(self):
        return self.get_element_text(how='xpath', path="//div[@class='header-links']//a[contains(@href,'customer/info')]")

    def check_welcome_message_displayed(self, message):
        return self.does_element_exist(how='xpath', path=f"//h2[contains(text(),'{message}')]")

    # use this method to click, pass as options:- 'Register', 'Log in', 'Shopping Cart', 'Wishlist'
    def click_header_options(self, options):
        self.click_element(how='xpath', path=f"//a[contains(text(),'{options}')]")

    def login_as_user(self, email, password ):
        self.fill_out_text_field(by_locator=self.EMAIL_FIELD, value=email)
        self.fill_out_text_field(by_locator=self.PASSWORD_FIELD, value=password)
        self.checkbox_by_label(how='xpath', label_path="//input[@id='RememberMe']", checkbox_path="//input[@id='RememberMe']/following-sibling::label")
        self.click_element(by_locator=self.LOGIN_BUTTON)

    def click_register_button(self):
        self.click_element(how='xpath', path=f"//input[@value='Register']")

    def get_registration_error_message(self):
        return self.get_element_text(how='xpath', path="//div[@class='message-error']//li")

    def take_survey_community_poll(self, option):
        self.checkbox_by_label(how='xpath',label_path=f"//label[contains(text(),'{option}')]", checkbox_path=f"//label[contains(text(),'{option}')]/../input")
        self.click_element(how='xpath', path=f"//input[@id='vote-poll-1']")

    def get_poll_results(self):
        return self.get_elements_text(how='xpath', path="//ul[@class='poll-results']")

    def add_products_from_dashboard_page(self, product):
        self.click_element(how='xpath', path=f"//a[contains(text(),'{product}')]/../following-sibling::div//input")

        self.wait(15)
        product_details = []
        product_name = self.get_element_text(how='xpath', path=f"//div[@class='overview']/div[@class='product-name']")
        product_details.append(product_name)
        product_description = self.get_element_text(how='xpath', path=f"//div[@class='overview']/div[@class='short-description']")
        product_details.append(product_description)
        return product_details

    def get_prefilled_name_and_email_address(self):
        prefilled_value = []
        name = self.get_elements_attribute(how='xpath', path="//label[text()='Your Name:']/following-sibling::input", attribute='value')
        prefilled_value.append(name)
        email = self.get_elements_attribute(how='xpath', path="//label[text()='Your Email:']/following-sibling::input",
                                           attribute='value')
        prefilled_value.append(email)
        return prefilled_value

    def fill_recipient_name_and_email_address(self, recipient_name, recipient_email, message, quantity):
        self.wait(10)

        self.fill_out_text_field_date_picker_no_locator(how='xpath', path=f"(//label[contains(text(),'Recipient')]/following-sibling::input)[1]",string=recipient_name)
        self.fill_out_text_field_date_picker_no_locator(how='xpath',
                                                        path=f"(//label[contains(text(),'Recipient')]/following-sibling::input)[2]",
                                                        string=recipient_email)


        self.fill_out_text_field_date_picker_no_locator(how='xpath',
                                                        path="//label[text()='Qty:']/following-sibling::input",
                                                        string=quantity)

        self.add_to_cart_in_product_page()

    def get_error_message_while_adding_product(self):
        return self.get_elements_text(how='xpath', path="//div[@id='bar-notification']")


    def add_to_cart_in_product_page(self):
        self.wait(timeout=15)
        self.click_element(how='xpath', path="//div[@class='overview']/div[@class='product-name']/..//input[@value='Add to cart']")









