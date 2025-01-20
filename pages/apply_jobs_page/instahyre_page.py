from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.utils import dump_json

from pages.base_page import BasePage



class InstahyrePage(BasePage):
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
    def __init__(self, driver, title="insthyre Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['instahyre']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    # UI Automation

    # Login
    def login_to_instahyre(self, email, password):
        self.click_element(how='xpath', path="//a[text()='Login']")
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='email']", value=email)
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='password']", value=password)
        self.click_element(how='xpath', path="//button[text()='Login']")

    def sign_out_to_instahyre(self):
        if self.does_element_exist(how='xpath', path="//a[text()='Sign out']"):
            self.click_element(how='xpath', path="//a[text()='Sign out']")


    def apply_jobs_in_dashboard_page(self):
        self.sleep(7)
        applied_jobs = []

        if self.does_element_exist(how='xpath', path="//button[@id='interested-btn']"):
            self.click_element(how='xpath', path="(//button[@id='interested-btn'])[1]")
            self.sleep(5)
            while self.does_element_exist(how='xpath', path="//div[@id='employer-summary']/h2"):
                self.sleep(4)
                if self.does_element_exist(how='xpath', path="//*[contains(text(),'No matching opportunities found')]"):
                    break
                applied_jobs.append(self.get_element_text(how='xpath', path="//div[@id='employer-summary']/h2"))
                self.click_element(how='xpath', path="(//button[text()='Apply'])[1]")

        else:
            return applied_jobs

        return applied_jobs


    def apply_other_opportunity_jobs(self, skills_1, skills_2, skills_3, skills_4, location_1, location_2, location_3):
        self.click_element(how='xpath', path="//a[@id='nav-candidates-opportunities']")
        self.sleep(5)
        if self.does_element_exist(how='xpath', path="(//*[contains(text(),'Search other jobs')])[2]"):
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath', path="//input[@id='skills-selectized']", value=skills_1)
            self.click_element(how='xpath', path="//*[text()='Skills']")
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='skills-selectized']",
                                                                       value=skills_2)
            self.click_element(how='xpath', path="//*[text()='Skills']")
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='skills-selectized']",
                                                                       value=skills_3)
            self.click_element(how='xpath', path="//*[text()='Skills']")
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='skills-selectized']",
                                                                       value=skills_4)
            self.click_element(how='xpath', path="//*[text()='Skills']")

            # selecting location
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='locations-selectized']",
                                                                       value=location_1)
            self.click_element(how='xpath', path=f"//div[@data-value='{location_1}']")
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='locations-selectized']",
                                                                       value=location_2)
            self.click_element(how='xpath', path=f"//div[@data-value='{location_2}']")
            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='locations-selectized']",
                                                                       value=location_3)
            self.click_element(how='xpath', path=f"//div[@data-value='{location_3}']")

            el = self.get_web_elements(how='xpath', path="//input[@id='years']")
            self.scroll_to_js(el[0])

            self.fill_out_text_field_no_locator_for_applying_instahyre(how='xpath',
                                                                       path="//input[@id='years']",
                                                                       value='3')

            self.click_element(how="xpath", path="//button[@id='show-results']")
            self.sleep(5)


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









