from selenium.webdriver.common.keys import Keys
import re

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.utils import dump_json

from pages.base_page import BasePage
from utils.file_helpers import get_file_from_import_testing_folder
import pyautogui

class NaukriPage(BasePage):
    # region Locators
    FIRST_NAME_FIELD = By.ID, "FirstName"
    LAST_NAME_FIELD = By.ID, "LastName"
    EMAIL_FIELD = By.ID, "Email"
    PASSWORD_FIELD = By.ID, "Password"
    CONFIRM_PASSWORD_FIELD = By.ID, "ConfirmPassword"
    REGISTER_BUTTON = By.ID, "register-button"
    LOGIN_BUTTON = By.XPATH, "//input[@value='Log in']"
    UPLOAD_FILE = By.XPATH, "//input[@value='Update resume']"

    # endregion Locators
    #saucedemo Login


    # page class constructor
    def __init__(self, driver, title="insthyre Login"):
        super().__init__(driver)
        self.url = self.config['base_urls']['naukri']
        self.title = title

    # region General Page Actions

    def goto(self):
        self.goto_page(self.url)

    # UI Automation

    # Login
    def login_to_naukri(self, email, password):
        self.wait_for_loading_animation()
        self.sleep(7)
        self.click_element(how='xpath', path="//a[@id='login_Layer']")
        self.fill_out_text_field_no_locator(how='xpath', path="//label[text()='Email ID / Username']/following-sibling::input", value=email)
        self.fill_out_text_field_no_locator(how='xpath', path="//label[text()='Password']/following-sibling::input", value=password)
        self.click_element(how='xpath', path="//button[text()='Login']")
        self.wait_for_loading_animation()
        self.sleep(7)

    def click_jobs(self):
        self.click_element(how='xpath', path="//div[text()='Jobs']")

    def apply_jobs_in_naukri(self):
        self.wait_for_loading_animation()
        self.sleep(2)
        if self.does_element_exist(how='xpath', path=f"//a[@class='view-all-link']/span"):
            self.click_element(how='xpath', path=f"//a[@class='view-all-link']/span")
            self.wait_for_loading_animation()
            self.sleep(7)
            self.click_element(how='xpath', path="//div[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader']")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(7)

        elif self.does_element_exist(how='xpath', path=f"//*[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader']"):
            self.click_element(how='xpath', path="//*[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader']")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(7)




        if self.does_element_exist(how='xpath', path="(//button[@id='apply-button'])[1]"):
            self.click_element(how="xpath", path="(//button[@id='apply-button'])[1]")
            self.wait_for_loading_animation()
            self.sleep(4)
            # if Drawer is detected:-
            if self.does_element_exist(how='xpath', path="//div[contains(@id,'Drawer')]"):
                val = self.complete_drawer_questions()
                if val == 'Thank you for your responses' or  val == 'Thankyou for your responses':
                    return val
                print("applied Jobs")

            self.close_popup()
            self.switch_to_new_window(main_window=True)
            return

        elif self.does_element_exist(how='xpath', path="(//button[@id='company-site-button'])[1]"):
            self.close_popup()
            self.switch_to_new_window(main_window=True)
            return

        else:
            self.click_element(how='xpath', path="(//div[@class='srp-jobtuple-wrapper'])[1]")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(10)

            if self.short_check_for_displayed_elements(how='xpath', path="(//button[@id='apply-button'])[1]"):
                self.click_element(how="xpath", path="(//button[@id='apply-button'])[1]")
                self.wait_for_loading_animation()
                self.sleep(3)
                # if Drawer is detected:-
                if self.does_element_exist(how='xpath', path="//div[contains(@id,'Drawer')]"):
                    val = self.complete_drawer_questions()

                    if val == 'Thank you for your responses' or  val == 'Thankyou for your responses':
                        return val
                    print("applied jobs")

                self.close_popup()
                self.switch_to_new_window(main_window=True)
                return

            elif self.does_element_exist(how='xpath', path="(//button[@id='company-site-button'])[1]"):
                self.close_popup()
                self.switch_to_new_window(main_window=True)

                return

    def complete_drawer_questions(self, radio_button_option='Yes', first_name = 'Ankit', last_name = 'Bharti', city='Bangalore', cgpa ='8.17'):
        self.wait_for_loading_animation()
        self.sleep(4)

        radio_button_list_expected_question = ['Do You have Experience', 'Worked for', 'Privacy Agreement', 'Are you currently', 'Are you willing']
        yes_or_no_input_field_expected_questions = ['Do You have Experience', 'Are you currently', 'Can you attend','Worked for','would you be able to', 'Would you be able to', 'Do you have hands', 'Can you join', 'Can you come for interview', 'Hands on exp']
        input_field_list_of_expected_questions = [ 'Privacy Agreement']
        if self.does_element_exist(how='xpath', path="(//div[contains(@id,'Messages')])[1]") and self.does_element_exist(how='xpath', path="(//div[contains(@class, 'Message')])[1]"):


            # scnenario 1 :
            if self.does_element_exist(how='xpath', path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[2]"):
                i =2

                while self.does_element_exist(how='xpath', path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[{i}]"):

                    question = self.get_element_text(how='xpath',path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[{i}]")
                    i += 2

                    if 'Please read the privacy content and confirm.' in question:
                        self.click_element(how='xpath', path="//span[text()='Yes']")
                        self.wait_for_loading_animation()
                        self.sleep(4)
                        return

                    if self.does_element_exist(how='xpath', path="//div[contains(@id, 'SingleSelectRadioButton')]//label"):
                        self.complete_radio_button_related_questions()

                    elif self.does_element_exist(how='xpath', path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]"):
                        val = self.complete_the_questions(yes_or_no_input_field_expected_questions=yes_or_no_input_field_expected_questions, question=question )

                        if val == 'Thank you for your responses' or val == 'Thankyou for your responses':
                            return val

                    elif self.does_element_exist(how='xpath', path="(//div[contains(@id, 'checkboxes')]//label)[1]"):
                        self.complete_checkbox_related_questions()

                self.wait_for_loading_animation()
                self.sleep(2)

            # scnenario 2 :
            elif self.does_element_exist(how='xpath', path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[1]"):
                i = 1

                while self.does_element_exist(how='xpath',
                                            path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[{i}]"):

                    question = self.get_element_text(how='xpath',
                                                     path=f"(//div[contains(@class, 'Message')]//div[contains(@class,'msg')]//span)[{i}]")
                    i += 2



                    if self.does_element_exist(how='xpath', path="//div[contains(@id, 'SingleSelectRadioButton')]//label"):
                        self.complete_radio_button_related_questions()

                    elif self.does_element_exist(how='xpath', path="(//div[contains(@id, 'checkboxes')]//label)[1]"):
                        self.complete_checkbox_related_questions()

                    elif self.does_element_exist(how='xpath',
                                                 path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]"):
                        val = self.complete_the_questions(yes_or_no_input_field_expected_questions=yes_or_no_input_field_expected_questions, question=question)

                        if val == 'Thank you for your responses' or val == 'Thankyou for your responses':
                            return val
                self.wait_for_loading_animation()
                self.sleep(2)

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

    def complete_the_questions(self, yes_or_no_input_field_expected_questions, question):

        if 'First' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Ankit')
            self.click_save_in_questianare()
            return

        elif 'Middle' in question:
            el = self.get_web_elements(how='xpath',
                                   path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='.')
            self.click_save_in_questianare()
            return

        elif 'Last' in question:
            el = self.get_web_elements(how='xpath',
                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                            path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                            value='Bharti')
            self.click_save_in_questianare()
            return

        elif 'Date of Birth' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='12/12/1999')
            self.click_save_in_questianare()
            return

        elif 'passing year' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='2022')
            self.click_save_in_questianare()
            return

        elif 'experience' in question or 'Experience' in question:

            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value="3")
            self.click_save_in_questianare()
            return

        elif 'Are you willing' in question or 'are you available' in question or 'available' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Yes')
            self.click_save_in_questianare()
            return



        elif 'City' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Bengaluru')
            self.click_save_in_questianare()
            return

        elif 'Location' in question or 'location' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Bengaluru')
            self.click_save_in_questianare()
            return

        elif 'Skills' in question or 'skills' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Python, Java, Selenium, Automation, API Testing')
            self.click_save_in_questianare()
            return

        elif 'Aadhaar' in question or 'aadhaar' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='675124254380')
            self.click_save_in_questianare()
            return


        elif 'reason for a Job change' in question or 'Job change' in question or 'job change' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='Career Growth')
            self.click_save_in_questianare()
            return

        elif 'Have you given any interview' in question or 'applied with us' in question or 'Have you applied' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='No')
            self.click_save_in_questianare()
            return

        elif 'CGPA' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value='8.17')
            self.click_save_in_questianare()
            return

        elif 'Percentage' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value="8.17")
            self.click_save_in_questianare()
            return

        elif 'Pan Card' in question or 'PAN' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value="EHFPB4599R")
            self.click_save_in_questianare()
            return

        elif 'How many years of experience' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value=3)
            self.click_save_in_questianare()
            return

        elif 'Official Notice' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                value="2 Months")
            self.click_save_in_questianare()
            return

        elif 'Current CTC'  in question or 'current CTC' in question or 'current annual CTC' in question:
            el = self.get_web_elements(how='xpath',
                                        path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="10")
            self.click_save_in_questianare()
            return

        elif 'Expected CTC' in question  or 'expected annual CTC' in question or 'expected CTC' in question or 'expected annual CTC' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="12")
            self.click_save_in_questianare()
            return

        elif 'pay' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="10")
            self.click_save_in_questianare()
            return

        elif 'other offer' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="No")
            self.click_save_in_questianare()
            return

        elif 'exp' in question or 'Exp' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="3")
            self.click_save_in_questianare()
            return



        elif 'If Yes' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="N/A")
            self.click_save_in_questianare()
            return

        elif 'Notice Period' in question or 'notice period' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="1 month")
            self.click_save_in_questianare()
            return

        elif 'Language' in question or 'Languages' in question or 'languages' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="1 month")
            self.click_save_in_questianare()
            return

        elif 'Institute' in question or 'College' in question or 'university' in question:
            el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
            self.scroll_to_js(el[0])
            self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value="Dayananda Sagar College Of Engineering")
            self.click_save_in_questianare()
            return

        elif 'Thank you for your responses' in question or 'Thankyou for your responses' in question:
            return 'Thank you for your responses' or 'Thankyou for your responses'

        for i in yes_or_no_input_field_expected_questions:
            if i in question:
                el = self.get_web_elements(how='xpath',
                                           path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]")
                self.scroll_to_js(el[0])
                self.fill_out_text_field_no_locator(how='xpath',
                                                    path="//div[contains(@id, 'InputBox')]//div[contains(@data-placeholder, 'Type message')]",
                                                    value='Yes')

                self.click_save_in_questianare()

        self.wait_for_loading_animation()
        self.sleep(2)

    def complete_checkbox_related_questions(self):
        self.wait_for_loading_animation()
        self.sleep(2)
        self.checkbox_by_label(how='xpath', checkbox_path=f"(//div[contains(@id, 'checkboxes')]//label//../input)[1]", label_path="(//div[contains(@id, 'checkboxes')]//label)[1]")

        self.sleep(2)
        self.click_save_in_questianare()

    def complete_radio_button_related_questions(self):
        self.wait_for_loading_animation()
        self.sleep(2)
        self.checkbox_by_label(how='xpath', checkbox_path=f"(//div[contains(@id, 'SingleSelectRadioButton')]//label//../input)[1]", label_path="(//div[contains(@id, 'SingleSelectRadioButton')]//label)[1]")

        self.sleep(2)
        self.click_save_in_questianare()


    def click_save_in_questianare(self):
        if self.does_element_exist(how='xpath', path="//div[@class='send']"):
            self.sleep(2)
            self.click_element(how='xpath', path="//div[@class='send']")
            self.wait_for_loading_animation()
            self.sleep(1)


    def update_profile_in_naukri(self, resume_name):
        self.click_element(how='xpath', path="(//div[contains(@class,'drawer')])[1]")
        self.wait_for_loading_animation()
        self.sleep(2)
        self.click_element(how='xpath', path="//a[contains(text(),'View & Update Profile')]")
        self.wait_for_loading_animation()
        self.sleep(2)
        self.upload_resume_in_naukri(resume_name)


    def update_profile_values_in_naukri(self, resume_header, skills_to_remove, skills_to_add):
        self.wait_for_loading_animation()
        self.click_element(how='xpath', path="(//div[contains(@class,'drawer')])[1]")
        self.wait_for_loading_animation()
        self.sleep(2)
        self.click_element(how='xpath', path="//a[contains(text(),'View & Update Profile')]")
        self.wait_for_loading_animation()
        self.click_element(how='xpath', path="//span[text()='Resume headline']/following-sibling::span")
        self.sleep(4)
        self.fill_out_text_field_no_locator(how='xpath', path="//textarea[@id='resumeHeadlineTxt']", value=resume_header)
        self.click_element(how='xpath', path="//button[text()='Save']")
        self.wait_for_loading_animation()
        self.sleep(3)


        # Adding skills
        self.click_element(how='xpath', path="//span[text()='Key skills']/following-sibling::span")
        self.sleep(4)
        self.click_element(how='xpath', path=f"//span[text()='{skills_to_remove[0]}']/following-sibling::a")

        self.sleep(2)
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='keySkillSugg']", value=skills_to_add[0])

        self.click_element(how='xpath', path="//button[text()='Save']")
        self.wait_for_loading_animation()
        self.sleep(3)

        # Adding skills again
        self.click_element(how='xpath', path="//span[text()='Key skills']/following-sibling::span")

        self.sleep(2)
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='keySkillSugg']", value=skills_to_remove[0])

        if self.does_element_exist(how='xpath', path="//button[text()='Save']"):
            self.click_element(how='xpath', path="//button[text()='Save']")
        self.wait_for_loading_animation()
        self.sleep(3)


    #     Adding Employment details
        self.click_element(how='xpath', path="//span[text()='Software Qa Engineer 2']/following-sibling::span")

        self.sleep(2)
        self.fill_out_text_field_no_locator(how='xpath', path="//input[@id='keySkillSugg']", value=skills_to_remove[0])

        self.click_element(how='xpath', path="//button[text()='Save']")
        self.wait_for_loading_animation()
        self.sleep(3)




    def upload_resume_in_naukri(self, file_name):
        self.wait_for_loading_animation()

        self.sleep(4)
        self.upload_a_file(path="//input[@value='Update resume']", file_name=file_name)
        self.sleep(2)



    def apply_jobs_in_naukri_in_recommended_section(self, option, no=2):
        self.wait_for_loading_animation()
        self.sleep(2)
        if self.does_element_exist(how='xpath', path=f"//a[@class='view-all-link']/span"):
            self.click_element(how='xpath', path=f"//a[@class='view-all-link']/span")
            self.wait_for_loading_animation()
            self.sleep(7)

            self.click_element(how='xpath', path=f"//div[contains(text(),'{option}')]")
            self.click_element(how='xpath',
                               path=f"(//div[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader'])[{no}]")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(7)

        elif self.does_element_exist(how='xpath',
                                     path=f"//*[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader']"):
            self.click_element(how='xpath',
                               path=f"(//*[contains(text(),'You might like')]/ancestor::section[@id='reco-header']/following-sibling::div//div[@class='jobTupleHeader'])[{no}]")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(7)

        if self.does_element_exist(how='xpath', path="(//button[@id='apply-button'])[1]"):
            self.click_element(how="xpath", path="(//button[@id='apply-button'])[1]")
            self.wait_for_loading_animation()
            self.sleep(4)
            # if Drawer is detected:-
            if self.does_element_exist(how='xpath', path="//div[contains(@id,'Drawer')]"):
                val = self.complete_drawer_questions()
                if val == 'Thank you for your responses' or val == 'Thankyou for your responses':
                    return val
                print("applied Jobs")

            self.close_popup()
            self.switch_to_new_window(main_window=True)
            return

        elif self.does_element_exist(how='xpath', path="(//button[@id='company-site-button'])[1]"):
            self.close_popup()
            self.switch_to_new_window(main_window=True)
            return

        else:
            self.click_element(how='xpath', path="(//div[@class='srp-jobtuple-wrapper'])[1]")
            self.switch_to_new_window()
            self.wait_for_loading_animation()
            self.sleep(10)

            if self.short_check_for_displayed_elements(how='xpath', path="(//button[@id='apply-button'])[1]"):
                self.click_element(how="xpath", path="(//button[@id='apply-button'])[1]")
                self.wait_for_loading_animation()
                self.sleep(3)
                # if Drawer is detected:-
                if self.does_element_exist(how='xpath', path="//div[contains(@id,'Drawer')]"):
                    val = self.complete_drawer_questions()

                    if val == 'Thank you for your responses' or val == 'Thankyou for your responses':
                        return val
                    print("applied jobs")

                self.close_popup()
                self.switch_to_new_window(main_window=True)
                return

            elif self.does_element_exist(how='xpath', path="(//button[@id='company-site-button'])[1]"):
                self.close_popup()
                self.switch_to_new_window(main_window=True)

                return





