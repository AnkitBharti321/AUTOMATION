import random

import pytest

from pages.apply_jobs_page.instahyre_page import InstahyrePage
from pages.apply_jobs_page.naukri_page import NaukriPage
from pages.apply_jobs_page.wellfound_page import WellfoundPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest

class TestApplyJobs(BaseTest):

    def test_apply_jobs_on_instahyre(self):
        assert_array = []
        instahyre_page = InstahyrePage(driver=self.driver, title='Instahyre login')
        instahyre_page.goto()
        instahyre_page.login_to_instahyre(email="ankitbharti7012@gmail.com", password="Aaum7012@123")
        applied_jobs = instahyre_page.apply_jobs_in_dashboard_page()
        print(applied_jobs)
        instahyre_page.apply_other_opportunity_jobs(skills_1="SDET", skills_2="Quality Assurance", skills_3="software qa", skills_4="Automation Testing", location_1="Work From Home", location_2="Bangalore", location_3="Hyderabad")
        applied_jobs_in_other_opportunities = instahyre_page.apply_jobs_in_dashboard_page()
        print(applied_jobs_in_other_opportunities)

        instahyre_page.sign_out_to_instahyre()

        assert not assert_array, assert_array

    def test_apply_jobs_on_instahyre_2(self):
        assert_array = []
        instahyre_page = InstahyrePage(driver=self.driver, title='Instahyre login')
        instahyre_page.goto()
        instahyre_page.login_to_instahyre(email="ankitbharti7012@gmail.com", password="Aaum7012@123")
        applied_jobs = instahyre_page.apply_jobs_in_dashboard_page()
        print(applied_jobs)
        instahyre_page.apply_other_opportunity_jobs(skills_1="software qa", skills_2="Quality Assurance", skills_3="SDET", skills_4="Automation Testing", location_1="Work From Home", location_2="Bangalore", location_3=None)
        applied_jobs_in_other_opportunities = instahyre_page.apply_jobs_in_dashboard_page()
        print(applied_jobs_in_other_opportunities)

        instahyre_page.sign_out_to_instahyre()

        assert not assert_array, assert_array

    def test_update_profile_on_instahyre(self):
        assert_array = []
        instahyre_page = InstahyrePage(driver=self.driver, title='Instahyre login')
        instahyre_page.goto()
        instahyre_page.login_to_instahyre(email="ankitbharti7012@gmail.com", password="Aaum7012@123")

        instahyre_page.update_instahyre_job_preferences(location_1="Bangalore")
        # instahyre_page.remove_locations(option="Bangalore")
        # instahyre_page.update_instahyre_job_preferences(location_1="Hyderabad")
        instahyre_page.sign_out_to_instahyre()


        assert not assert_array, assert_array

    @pytest.mark.apply_naukri_jobs
    def test_apply_job_in_naukri(self):
        assert_array = []
        naukri_page = NaukriPage(driver=self.driver, title='Naukri login')
        naukri_page.goto()
        naukri_page.login_to_naukri(email="ankitbharti7012@gmail.com", password="Aaum7012@123")
        for i in range(0, 10):
            naukri_page.goto()
            naukri_page.apply_jobs_in_naukri()
            naukri_page.refresh_page()
        a = 5

    @pytest.mark.apply_naukri_jobs
    def test_apply_job_in_naukri_in_recommeded_section(self):
        assert_array = []
        apply_options = ['You might like', 'Preferences', 'Applies']
        naukri_page = NaukriPage(driver=self.driver, title='Naukri login')
        naukri_page.goto()
        naukri_page.login_to_naukri(email="ankitbharti7012@gmail.com", password="Aaum7012@123")
        for i in apply_options:
            naukri_page.goto()
            naukri_page.apply_jobs_in_naukri_in_recommended_section(option=i)
            naukri_page.refresh_page()
        a = 5

    def test_update_profile_in_naukri(self):
        assert_array = []
        resume_name = ["AnkitBharti7012", "Ankit_resume"]
        skills_to_remove_and_readd = ["Cicd Pipeline"]
        skills_to_add = ["Regression Testing"]
        resume_header = ["A highly motivated Quality Assurance and Automation Test Engineer with over 3 years experience in software industry, centered in software testing around selenium Automation, Manual, API testing along with Performance testing using Apache JMeter along with troubleshooting, and deploying software solutions. Ability to learn quickly, often in high pressure situations, in order to fully understand a new product, platform or any mixture of the two.", "Detail-oriented and enthusiastic Software Development Engineer in Test (SDET) with a solid foundation in programming and automation testing with over 3 years experience. Seeking to leverage my knowledge of Python, Java, Selenium, and SQL in a dynamic testing environment to ensure high- quality software products"]
        naukri_page = NaukriPage(driver=self.driver, title='Naukri login')
        naukri_page.goto()
        naukri_page.login_to_naukri(email="ankitbharti7012@gmail.com", password="Aaum7012@123")
        naukri_page.update_profile_values_in_naukri(resume_header=random.choice(resume_header),skills_to_remove= skills_to_remove_and_readd, skills_to_add=skills_to_add)
        a =5







