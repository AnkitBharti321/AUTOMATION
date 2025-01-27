from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.utils import dump_json

from pages.base_page import BasePage



class WellfoundPage(BasePage):
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
    def __init__(self, driver, title="Wellfound Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['wellfound']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    # UI Automation

    # Login
    def login_to_wellfound(self, email, password):
        self.click_element(how='xpath', path="(//a[text()='Log In'])[1]")
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='user_email']", value=email)
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='user_password']", value=password)
        self.click_element(how='xpath', path="//input[@type='submit']")

    def sign_out_to_instahyre(self):
        if self.does_element_exist(how='xpath', path="//a[text()='Sign out']"):
            self.click_element(how='xpath', path="//a[text()='Sign out']")


    def apply_jobs_in_wellfound_dashboard_page(self, interest):
        self.sleep(7)
        applied_jobs = []
        expected_roles = ['Senior QA Engineer', 'QA Engineer', 'Test Engineer']

        if self.does_element_exist(how='xpath', path="//a[@class='content-center']"):
            self.click_element(how='xpath', path="(//a[@class='content-center'])[1]")
            self.sleep(5)



            if self.does_element_exist(how='xpath', path="(//h4[contains(text(),'QA Engineer')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'QA Engineer')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]", value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()

            elif self.does_element_exist(how='xpath', path="(//h4[contains(text(),'Test Engineer')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'Test Engineer')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]",
                                                    value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()


            elif self.does_element_exist(how='xpath', path="(//h4[contains(text(),'Senior QA Engineer')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'Senior QA Engineer')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]",
                                                    value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()

            elif self.does_element_exist(how='xpath', path="(//h4[contains(text(),'QA Engineer')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'QA Engineer')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]",
                                                    value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()

            elif self.does_element_exist(how='xpath', path="(//h4[contains(text(),'Lead QA Engineer')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'Lead QA Engineer')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]",
                                                    value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()

            elif self.does_element_exist(how='xpath', path="(//h4[contains(text(),'Automation Tester')]/../../..//button)[2]"):

                self.click_element(how='xpath', path="(//h4[contains(text(),'Automation Tester')]/../../..//button)[2]")
                self.wait_for_loading_animation()
                self.sleep(4)
                self.fill_out_text_field_no_locator(how='xpath', path="//textarea[contains(@id,'input')]",
                                                    value=interest)
                self.wait_for_loading_animation()
                self.click_element(how='xpath', path="(//button[@type='submit'])[2]")
                self.refresh_page()


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







