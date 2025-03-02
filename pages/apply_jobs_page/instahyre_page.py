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
            if location_3:
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


    def update_instahyre_job_preferences(self, location_1):
        self.sleep(5)
        self.click_element(how='xpath', path="//a[text()='Profile']")
        self.sleep(10)
        self.wait_for_elements_to_be_displayed(how='xpath', path="//div[@id='job-preferences']//a[contains(@class,'edit-link')]")
        el = self.get_web_elements(how='xpath', path="//div[@id='job-preferences']//a[contains(@class,'edit-link')]")
        self.scroll_to_js(el[0])
        self.click_element(how='xpath', path="//div[@id='job-preferences']//a[contains(@class,'edit-link')]")
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='preferred-location-selectized']", value=location_1 )
        self.click_element(how='xpath', path=f"//label[text()='Where are you open to working?']/..//div[@data-value='{location_1}']")
        self.click_element(how='xpath', path=f"//button[@id='candidate-jsp-save-btn']")

    def remove_locations(self, option):
        self.click_element(how='xpath', path="//div[@id='job-preferences']//a[contains(@class,'edit-link')]")
        self.sleep(3)
        self.click_element(how='xpath', path=f"//div[text()='{option}']/a")
        self.click_element(how='xpath', path=f"//button[@id='candidate-jsp-save-btn']")







