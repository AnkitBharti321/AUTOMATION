from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from database_connections import organizations
from pages.base_page import BasePage

from faker import Faker

# API AUTOMATION
import requests
import random
import string

# from pages.organization.organization_page import OrganizationPage
# from pages.sys_admin.sys_admin_change_password_page import SysAdminChangePasswordPage
# from pages.sys_admin.sys_admin_my_account_page import SysAdminMyAccountPage
# from utils import database_helpers

class LoginPage(BasePage):
    # region Locators
    # USERNAME_FIELD = By.ID, "user_name"
    PASSWORD_FIELD = By.ID, "password"
    LOGIN_BUTTON_ELEMENT = By.ID, "logon_submit"
    NEED_HELP_EL = By.XPATH, '//*[@id="need_help_link"]'

    LOGIN_FAILED_ALERT = By.XPATH, "//span[@class='mt-2 message text-danger auth-alert-msg']"

    # Forgot Password section
    FORGOT_PASSWORD_FIELD = By.XPATH, "//*[@id='main_login']/div/div[3]/a"
    FORGOT_PASSWORD_USERNAME_FIELD = By.ID, "pass_username"
    EMAIL_FIELD = By.ID, "email_address"
    NEW_PASSWORD_FIELD = By.ID, "new_password"
    OLD_PASSWORD_FIELD = By.ID, "old_password"
    CONFIRM_PASSWORD_FIELD = By.ID, "confirm_password"
    SAVE_BUTTON = By.XPATH, "//button[text()='Save']"
    CHANGE_PASSWORD_BTN = By.ID, "change_passwordBtn"
    MOBILE_CHANGE_PASSWORD_BUTTON = By.ID, "saveBtn"

    UPDATE_CONTACT_INFO_SAVE_FIELD = By.XPATH, "//button[text()='Save']"
    CURRENT_PASSWORD_FIELD = By.ID, "cpassword"
    RETYPE_NEW_PASSWORD_FIELD = By.ID, "n2password"
    NEW_CHANGED_PASSWORD_FIELD = By.ID, "n1password"

    MFA_MESSAGE_FIELD = By.ID, "mfa_access_code"
    MFA_LOGIN_BUTTON = By.XPATH, "//input[@type='submit' and @value='Login']"

    PAGE_TITLE = By.XPATH, "//title"
    FORGOT_PASSWORD_LINK = By.ID, "forgot_password_link"
    ALERT_MESSAGE_EL = By.XPATH, "//div[@class='col alert-content']"

    # Need Help Workflows
    FORGOT_UN_RADIO_BUTTON = By.ID, "admin_username_option"
    FORGOT_PW_RADIO_BUTTON = By.ID, "admin_password_option"
    CONTINUE_BUTTON = By.ID, "admin_form_submit"
    EMAIL_TEXT_BOX = By.ID, "admin_email"
    USERNAME_TEXT_BOX = By.ID, "admin_username"

    NEW_PW_TEXT_BOX = By.ID, "n1password"
    VERIFY_PW_TEXT_BOX = By.ID, "n2password"
    CHANGE_PW_BUTTON = By.ID, "change_passwordBtn"
    USERNAME_LABEL = By.XPATH, "//span[contains(@class, 'user-name')]"

    FORGOT_USERNAME_RADIO_BUTTON = By.ID, "forgot_uname"
    FORGOT_PASSWORD_RADIO_BUTTON = By.XPATH, "//input[@id='forgot_password']"
    LAST_NAME_TEXT_BOX = By.ID, "last_name"
    DOB_TEXT_BOX = By.ID, "dob"
    SSN_TEXT_BOX = By.ID, "ssn"
    USER_NAME_TEXT_BOX = By.ID, "pass_username"
    ADMIN_USER_NAME_TEXT_BOX = By.ID, "admin_username"
    SUBMIT_FORM = By.ID, "submitForm"
    INVALID_SSN_EL = By.ID, "ssn_validation"

    EMP_CREDENTIALS_RETRIEVAL_RADIO_BUTTON = By.ID, "employee_selection"
    ADMIN_CREDENTIALS_RETRIEVAL_RADIO_BUTTON = By.ID, "admin_selection"
    NEED_HELP_CONTINUE_BUTTON = By.ID, "continue"

    # hcm dashboard login
    HCM_DASHBOARD_USERNAME = By.ID, "txtUserEmail"
    HCM_DASHBOARD_PASSWORD = By.ID, "txtUserPassword"
    HCM_DASHBOARD_SUBMIT = By.XPATH, "//button[@type='submit']"

    # Amazon search
    SEARCH_AMAZON = By.XPATH, "//input[@id='twotabsearchtextbox']"
    SEARCH_SUBMIT_BUTTON = By.XPATH, "//input[@id='nav-search-submit-button']"
    TEXT_SEARCHED_MOBILE_PHONE = By.XPATH, "//div[@cel_widget_id='MAIN-SEARCH_RESULTS-2']//div//h2"
    GO_TO_CART_PAGE = By.XPATH, "//div[@id='nav-cart-text-container']"
    TODAYS_DEAL = By.XPATH, "//a[@href='/deals?ref_=nav_cs_gb']"
    RADIO_BUTTON_PRICE = By.XPATH, "(//div//input[@name='price'])[2]"
    USER_NAME_SWAG = By.XPATH, "//input[@id = 'user-name']"
    PASSWORD_SWAG = By.XPATH, "//input[@id = 'password']"
    SUBMIT_BUTTON_SWAG = By.XPATH, "//input[@id='login-button']"

    # Make my trip
    CLOSE_LOGIN_CREATE_ACCOUNT_SCREEN = By.XPATH, "//span[@data-cy='closeModal']"

    # endregion Locators
    #saucedemo Login


    # page class constructor

    def __init__(self, driver, title="amazon Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['amazon']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    # UI Automation

    # Amazon

    def test_validate_mobile_search_in_amazon(self, value):
        self.fill_out_text_field(by_locator=self.SEARCH_AMAZON, value=value)
        self.click_element(by_locator = self.SEARCH_SUBMIT_BUTTON, ajax=False)
        text_searched_mobile_phone = self.get_element_text(by_locator=self.TEXT_SEARCHED_MOBILE_PHONE)
        return text_searched_mobile_phone

    def test_add_to_cart(self, buying_option):
        self.click_element(how="xpath",
                           path=f"//span[contains(text(),'{buying_option}')]//ancestor::a/../..//button",
                           ajax=False)
        self.click_element(by_locator=self.GO_TO_CART_PAGE, ajax=False)

    def test_validate_todays_deal(self, appliances, option_text):
        self.click_element(by_locator=self.TODAYS_DEAL, ajax=False)
        self.click_element(how="xpath", path=f"//span[text()='{appliances}']", ajax=False)
        self.checkbox_by_label(how='xpath', label_path=f"(//div//input[@name='price'])//parent::label/span/span[contains(text(),'{option_text}')]/ancestor::label",checkbox_path=f"(//div//input[@name='price'])//parent::label/span/span[contains(text(),'{option_text}')]/ancestor::label/input")

    # Swag

    def test_validate_login_swag(self, user_name, password):
        self.fill_out_text_field(self.USER_NAME_SWAG, user_name)
        self.fill_out_text_field(self.PASSWORD_SWAG, password)
        self.click_element(by_locator=self.SUBMIT_BUTTON_SWAG, ajax=False)

    # Make My Trip

    def test_close_login_create_account_screen(self):
        self.click_element(by_locator=self.CLOSE_LOGIN_CREATE_ACCOUNT_SCREEN, ajax=False)

    def test_search_flight_source_to_destination(self, source, loc):
        self.click_element(how='xpath', path=f"//span[text()='{source}']", ajax=True)
        self.click_element(how='xpath', path=f"//input[@placeholder='{source}']/parent::div//p[text()='{loc}']",
                           ajax=True)

    def test_search_flight_date(self, day, month, year):
        self.click_element(how='xpath', path=f"//span[text()='Departure']", ajax=False)
        self.click_element(how='xpath', path=f"//div[text()='{month} {year}']/ancestor::div[@class='DayPicker-Month']//p[text()='{day}']", ajax=False)
        self.click_element(how='xpath', path=f"//a[text()='Search']", ajax=False)

    def test_go_to_hotel_tab(self):
        self.click_element(how='xpath', path=f"//span[text()='Hotels']//ancestor::li[@class='menu_Hotels']", ajax=False)

    def test_search_hotel(self, location):
        self.click_element(how='xpath', path="//input[@id='city']", ajax=False)
        self.click_element(how='xpath', path=f"//input[@placeholder='Where do you want to stay?']/parent::div/following-sibling::div//span[text()='{location}']", ajax=False)

    def test_check_in_and_check_out_hotel(self, day, month, year):
        self.click_element(how='xpath',
                           path=f"//span[text()='{year}']/ancestor::div[@class='DayPicker-Month']//div[text()='{month}']/parent::div/following-sibling::div//div[text()='{day}']",
                           ajax=False)

    def test_select_rooms_and_guests(self, count_of_children, age_of_children):
        self.click_element(how='xpath', path="//span[@data-testid='children_count']", ajax=False)
        self.click_element(how='xpath', path=f"//li[text()='{count_of_children}']", ajax=False)
        self.click_element(how='xpath', path="//span[text()='Select']", ajax=False)
        self.click_element(how='xpath', path=f"//li[text()='{age_of_children}']", ajax=False)
        self.click_element(how='xpath', path="//button[text()='Apply']", ajax=False)
        self.click_element(how='xpath', path="//button[text()='Search']", ajax=False)

    # API Automation

    def get_request(self, base_url, auth_token):
        resources_url = base_url + "/public/v2/users/"
        headers = {"Authorization": auth_token}
        get_response = requests.get(url=resources_url, headers=headers)
        return get_response

    def post_request(self, base_url, auth_token):
        resource_url = base_url + "/public/v2/users/"
        headers = {"Authorization": auth_token}
        fake = Faker()
        data = {
            "name": "RJyoti",
            "email": f"{fake.email()}",
            "gender": "male",
            "status": "active"
        }
        post_response = requests.post(resource_url, data=data, headers=headers)
        return post_response

    def put_request(self, base_url, auth_token, user_id):
        resource_url = base_url + f"/public/v2/users/{user_id}"
        headers = {"Authorization": auth_token}
        fake = Faker()
        data = {
            "name": "JyotiRanjan",
            "email": f"{fake.email()}",
            "gender": "male",
            "status": "active"
        }
        put_response = requests.put(url=resource_url, data=data, headers=headers)
        return put_response

    def delete_request(self, base_url, auth_token, id):
        url = base_url + f"/public/v2/users/{id}"
        headers = {"Authorization": auth_token}

        response = requests.delete(url=url, headers=headers)
        return response














    # def get_api_request(self, base_url, auth_token):
    #     url = base_url + "/public/v2/users/"
    #     headers = {"Authorization": auth_token}
    #     response = requests.get(url=url, headers=headers)
    #     return response
    #
    # def post_api_request(self, base_url, auth_token):
    #     url = base_url + "/public/v2/users/"
    #     headers = {"Authorization": auth_token}
    #     data = {
    #         "name": "Jyoti",
    #         "email": "routjyotiranjan4654@gmail.com",
    #         "gender": "male",
    #         "status": "active"
    #     }
    #
    #     response = requests.post(url=url,data=data ,headers=headers)
    #     return response
    #
    # def put_api_request(self, base_url, auth_token, id):
    #     url = base_url + f"/public/v2/users/{id}"
    #     headers = {"Authorization": auth_token}
    #     data = {
    #         "name": "Jyoti Ranjan",
    #         "email": "routjyotiranjan34567890876@gmail.com",
    #         "gender": "male",
    #         "status": "active"
    #     }
    #
    #     response = requests.put(url=url, data=data, headers=headers)
    #     return response
    #
    # def delete_api_request(self, base_url, auth_token, id):
    #     url = base_url + f"/public/v2/users/{id}"
    #     headers = {"Authorization": auth_token}
    #
    #     response = requests.delete(url=url, headers=headers)
    #     return response

    def goto_with_org_code(self, org_code, reuse_username=False, custom_login=False):
        if reuse_username and custom_login:
            self.goto_page(f"{self.url}/logon/{org_code}/?{org_code}")
        elif custom_login:
            self.goto_page(f"{self.url}/logon/?{org_code}")
        else:
            self.goto_page(f"{self.url}/logon/{org_code}")

    def username(self, value):
        self.fill_out_text_field(self.USERNAME_FIELD, value)

    def get_username_text(self):
        return self.get_text_field_text(self.USERNAME_FIELD)

    def password(self, value):
        self.fill_out_text_field(self.PASSWORD_FIELD, value)

    def login_button(self, ajax=True):
        timing = self.click_element(self.LOGIN_BUTTON_ELEMENT, ajax=ajax)
        return timing

    def click_need_help_link(self):
        self.click_element(self.NEED_HELP_EL)

    def get_alert_message(self):
        return self.get_element_text(self.ALERT_MESSAGE_EL)

    def forgot_password(self):
        self.click_element(self.FORGOT_PASSWORD_LINK)

    def forgot_password_username(self, value):
        self.fill_out_text_field(self.FORGOT_PASSWORD_USERNAME_FIELD, value)

    def email(self, value):
        self.fill_out_text_field(self.EMAIL_FIELD, value)

    def new_password_button(self):
        self.click_element(self.NEW_PASSWORD_FIELD)

    def old_password(self, value):
        self.fill_out_text_field(self.OLD_PASSWORD_FIELD, value)

    def new_password(self, value):
        self.fill_out_text_field(self.NEW_PASSWORD_FIELD, value)

    def confirm_password(self, value):
        self.fill_out_text_field(self.CONFIRM_PASSWORD_FIELD, value)

    def save(self):
        self.click_element(self.SAVE_BUTTON)

    def username_hcm_dashboard(self, value):
        self.fill_out_text_field(self.HCM_DASHBOARD_USERNAME, value)

    def password_hcm_dashboard(self, value):
        self.fill_out_text_field(self.HCM_DASHBOARD_PASSWORD, value)

    def submit_hcm_dashboard(self):
        self.click_element(self.HCM_DASHBOARD_SUBMIT, ajax=False)

    # todo add alert check to the click element function
    def update_contact_info_save(self):
        self.click_element(self.UPDATE_CONTACT_INFO_SAVE_FIELD)

    def current_password(self, value):
        self.fill_out_text_field(self.CURRENT_PASSWORD_FIELD, value)

    def retype_new_password(self, value):
        self.fill_out_text_field(self.RETYPE_NEW_PASSWORD_FIELD, value)

    def new_changed_password(self, value):
        self.fill_out_text_field(self.NEW_CHANGED_PASSWORD_FIELD, value)

    def new_changed_password_btn(self, ajax=True):
        self.click_element(self.CHANGE_PASSWORD_BTN, ajax=ajax)

    def click_mobile_change_password_btn(self, ajax=True):
        self.click_element(self.MOBILE_CHANGE_PASSWORD_BUTTON, ajax=ajax)

    def new_changed_password_btn_displayed(self):
        return self.element_displayed(self.CHANGE_PASSWORD_BTN)

    def fill_mfa_message_text_field(self, value):
        self.fill_out_text_field(self.MFA_MESSAGE_FIELD, value)

    def click_mfa_login_button(self):
        self.click_element(self.MFA_LOGIN_BUTTON)

    # endregion General Page Actions

    global login_org_name
    login_org_name = None

    def login(self, username, password, ajax=True):
        self.goto()
        self.username(username)
        self.password(password)
        timing = self.login_button(ajax=ajax)
        if self.get_element_attribute(self.PAGE_TITLE, "innerText", wait=2) == "Dashboard":
            global login_org_name
            login_org_name = self.get_org_name()
        else:
            login_org_name = None
        return timing

    def goto_analytics(self):
        self.goto_page(self.config['base_urls']['analytics'])

    def analytics_login(self, username, password):
        self.goto_analytics()
        self.username(username)
        self.password(password)
        self.login_button()

    def goto_emp_credentials_recover_page(self):
        self.goto_page(self.emp_credentials_recover_page_url)

    def goto_admin_credentials_recover_page(self):
        self.goto_page(self.admin_credentials_recover_page_url)

    def safe_login(self, username, password):
        test_password = "TestPswdA@!2"
        my_account_page = SysAdminMyAccountPage(self.driver)
        change_password_page = SysAdminChangePasswordPage(self.driver)

        self.goto()
        self.username(username)
        self.password(password)
        self.login_button()

        if "changepassword" in self.driver.current_url:
            change_password_page.change_password_login_screen(password, test_password)
            my_account_page.goto()
            my_account_page.change_password_button()
            change_password_page.change_password(test_password, password)

        if "updatecontactinfo" in self.driver.current_url:
            self.click_element(self.UPDATE_CONTACT_INFO_SAVE_FIELD)

        if self.get_element_attribute(self.PAGE_TITLE, "innerText", wait=2) == "Dashboard":
            global login_org_name
            login_org_name = self.get_org_name()
        else:
            login_org_name = None

    # todo the twilio api needs to be set up to finish the mfa method
    def safe_mfa_login(self, username, password, phone_number, remember):
        test_password = "TestPswdA@!2"
        my_account_page = SysAdminMyAccountPage(self.driver)
        change_password_page = SysAdminChangePasswordPage(self.driver)

        self.goto()
        self.username(username)
        self.password(password)
        self.login_button()
        self.sleep(3)

    def safe_login_sys_admin(self, username, password):
        sys_admin_password = self.config['login']['sysadmin_password']
        my_account_page = SysAdminMyAccountPage(self.driver)
        change_password_page = SysAdminChangePasswordPage(self.driver)
        test_password = "TestPswdA@!2"

        self.goto()
        self.username(username)
        self.password(password)
        self.login_button()

        if "changepassword" in self.driver.current_url:
            change_password_page.change_password(sys_admin_password, test_password)
            my_account_page.goto()
            my_account_page.change_password_button()
            change_password_page.change_password(test_password, sys_admin_password)

    # region Specific Login Methods #
    def login_as_organization(self):
        username = self.config['organizations']['create_new_employee']['username']
        password = self.config['organizations']['create_new_employee']['password']

        return self.login(username, password)

    def login_as_root(self):
        self.safe_login(self.config['login']['root_username'], self.config['login']['root_password'])

    def login_as_old_ui_root(self):
        self.safe_login(self.config['login']['old_ui_root_username'], self.config['login']['old_ui_root_password'])

    def login_as_synthetic_root(self):
        self.safe_login(self.config['login']['root_synthetic_username'],
                        self.config['login']['root_synthetic_password'])

    def login_as_synthetic_broker(self):
        self.safe_login(self.config['login']['broker_synthetic_username'],
                        self.config['login']['broker_synthetic_password'])

    def login_as_broker(self):
        self.safe_login(self.config['login']['broker_username'], self.config['login']['broker_password'])

    def login_as_sysadmin(self):
        self.safe_login_sys_admin(self.config['login']['sysadmin_username'], self.config['login']['sysadmin_password'])

    def login_as_edi(self):
        self.safe_login(self.config['login']['edi_username'], self.config['login']['edi_password'])

    def login_as_subscriber(self):
        self.login(self.config['subscriber_username'], self.config['subscriber_password'])

    def login_as_subscriber_ui2(self):
        self.login(self.config['subscriber_username_ui2'], self.config['subscriber_password_ui2'])

    def login_as_ldex_admin(self):
        self.safe_login(self.config['login']['ldex_admin_username'], self.config['login']['ldex_admin_password'])

    def login_employee_with_default_password(self, added_employee, ajax=True, mobile=False):
        added_employee['password'] = re.sub("/", "", added_employee['birthdate'])
        self.login(added_employee['user_name'], added_employee['password'], ajax=ajax)
        if "/changepassword" in self.driver.current_url:
            self.set_new_password(added_employee['password'], "automation1", ajax=ajax, mobile=mobile)

    def login_employee_with_organisation_specific_url(self, employee, org_code, reuse_username=False, custom_login=False):
        self.goto_with_org_code(org_code, reuse_username, custom_login)
        employee['password'] = re.sub("/", "", employee['birthdate'])
        self.username(employee['user_name'])
        self.password(employee['password'])
        self.login_button()
        if "/changepassword" in self.driver.current_url:
            self.set_new_password(employee['password'], "automation1")

    def goto_hcm_dashboard(self):
        self.goto_page(f"{self.config['base_urls']['HCM_dashboard']}login")

    def hcm_dashboard_login(self):
        self.goto_hcm_dashboard()
        username = self.config['login']['hcm_dashboard_username']
        password = self.config['login']['hcm_dashboard_password']
        self.username_hcm_dashboard(username)
        self.password_hcm_dashboard(password)
        self.submit_hcm_dashboard()

    # endregion Specific Login Methods #

    # region Reset Password Methods #

    def set_new_password(self, old_password, new_password, ajax=True, mobile=None):
        self.current_password(old_password)
        self.new_changed_password(new_password)
        self.retype_new_password(new_password)
        if mobile:
            self.click_mobile_change_password_btn(ajax=ajax)
        else:
            self.new_changed_password_btn(ajax=ajax)

    # todo
    def recover_password_as_any(self, user_name, last_name, dob, ssn, new_password, user_type='subscriber'):
        self.click_need_help_link()
        self.click_employee_credentials_radio_button()
        self.click_need_help_continue_button()
        self.click_need_help_forgot_password_radio_button()
        if user_type == 'subscriber':
            self.enter_need_help_username(user_name)
        else:
            self.enter_admin_username(user_name)
        self.enter_lastname(last_name)
        self.enter_dob(dob)
        self.move_to_ssn_element()
        self.enter_ssn(ssn[-4:])
        self.submit_form()
        self.new_changed_password(new_password)
        self.retype_new_password(new_password)
        self.new_changed_password_btn()

    def recover_username_as_any(self, last_name, dob, ssn):
        self.click_need_help_link()
        self.click_employee_credentials_radio_button()
        self.click_need_help_continue_button()
        self.click_need_help_forgot_username_radio_button()
        self.enter_lastname(last_name)
        self.enter_dob(dob)
        self.move_to_ssn_element()
        self.enter_ssn(ssn[-4:])
        self.submit_form()

    # endregion Reset Password Methods #

    # region PS_ERROR Checker #
    def get_org_name(self):
        self.wait_for_ajax()
        login_org_name = self.get_elements_text('id', "footer-organization-name")
        return login_org_name[0]



    # region Logoff helpers

    def logoff_current_site(self):
        current_site = self.site_logged_into()
        if current_site == "sys_admin":
            self.__logoff_sysadmin_site()
        elif current_site == "subscriber":
            self.__logoff_subscriber_site()
        elif current_site == "broker":
            self.__logoff_broker_site()
        elif current_site == "admin":
            self.__logoff_admin_site()
        elif current_site == "benefits" or current_site == "ben_admin" or current_site == "aca":
            self.__logoff_ben_admin_site()


    def __logoff_ben_admin_site(self):
        org_page = OrganizationPage(self.driver)
        org_page.click_left_hand_nav_link("LOGOUT")

    def __logoff_broker_site(self):
        self.click_element(how="xpath", path="//div[@class='body_content']/table/tbody/tr/td[2]/div[2]/a")

    def __logoff_subscriber_site(self):
        self.click_element(how="xpath", path="//a[contains(text(),'Welcome')]")
        self.click_element(how="xpath", path="//a[contains(text(),'Welcome')]//following-sibling::ul//a[@href='/subscriber/logoff']")
        if self.short_check_for_displayed_elements("xpath", "//span[.='Confirm']/.."):
            self.click_element(how="xpath", path="//span[.='Confirm']/..")

    def __logoff_sysadmin_site(self):
        self.click_element(how="xpath", path="//div[@id='logonlink']/a")

    def __logoff_admin_site(self):
        self.click_element(how="xpath", path="//table[@class='tspace1 rspace2']/tbody/tr/td[2]/a")

    def site_logged_into(self):
        current_url = self.driver.current_url
        url_array = current_url.split("/")

        if len(url_array) >= 5:
            if url_array[4] == "sys_main":
                return "sys_admin"
        if url_array[3] == "subscriber":
            return "subscriber"
        if url_array[3] == "ben_admin":
            return "ben_admin"
        if url_array[3] == "aca":
            return "ben_admin"
        if url_array[3] == "broker":
            return "broker"
        if url_array[0] == "benefits":
            return "benefits"
        if url_array[0] == "admin":
            return "admin"
    # endregion Logoff helpers

    # region Need Help

    def emp_credentials_recover_page_url(self):
        return f"{self.config['base_urls']['benefits']}/logon_assist/assist_type"

    def click_forgot_username_radio_button(self):
        self.click_element(self.FORGOT_UN_RADIO_BUTTON)

    def click_forgot_password_radio_button(self):
        self.click_element(self.FORGOT_PW_RADIO_BUTTON)

    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)

    def enter_email(self, value):
        self.fill_out_text_field(self.EMAIL_TEXT_BOX, value)

    def enter_admin_username(self, value):
        self.fill_out_text_field(self.ADMIN_USER_NAME_TEXT_BOX, value)

    def enter_new_password(self, value):
        self.fill_out_text_field(self.NEW_PW_TEXT_BOX, value)

    def reenter_new_password(self, value):
        self.fill_out_text_field(self.VERIFY_PW_TEXT_BOX, value)

    def click_change_password_button(self):
        self.click_element(self.CHANGE_PW_BUTTON)

    def get_username_value(self):
        return self.get_element_text(self.USERNAME_LABEL)

    def click_need_help_forgot_username_radio_button(self):
        self.click_element(self.FORGOT_USERNAME_RADIO_BUTTON)

    def click_need_help_forgot_password_radio_button(self):
        self.click_element(self.FORGOT_PASSWORD_RADIO_BUTTON)

    def submit_form(self):
        self.click_element(self.SUBMIT_FORM)

    def enter_lastname(self, value):
        self.fill_out_text_field(self.LAST_NAME_TEXT_BOX, value)

    def enter_dob(self, value):
        self.fill_out_text_field_date_picker(self.DOB_TEXT_BOX, value)

    def move_to_ssn_element(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).perform()

    def enter_ssn(self, value):
        self.fill_out_text_field(self.SSN_TEXT_BOX, value)

    def enter_need_help_username(self, value):
        self.fill_out_text_field(self.USER_NAME_TEXT_BOX, value)

    def get_invalid_ssn_text(self):
        return self.get_element_text(self.INVALID_SSN_EL)

    def click_employee_credentials_radio_button(self):
        self.click_element(self.EMP_CREDENTIALS_RETRIEVAL_RADIO_BUTTON)

    def click_admin_credentials_radio_button(self):
        self.click_element(self.ADMIN_CREDENTIALS_RETRIEVAL_RADIO_BUTTON)

    def click_need_help_continue_button(self):
        self.click_element(self.NEED_HELP_CONTINUE_BUTTON)

    # endregion Need Help

    # region MFA
    def fill_out_two_step_verification(self, code):
        self.fill_out_text_field(self.MFA_MESSAGE_FIELD, code)
        self.click_element(self.MFA_LOGIN_BUTTON)

    def create_new_account(self):
        self.click_element(how="xpath", path="//a[contains(text(),'Create new account')]", ajax=False)

    # endregion MFA