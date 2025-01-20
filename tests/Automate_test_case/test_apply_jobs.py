import pytest

from pages.apply_jobs_page.instahyre_page import InstahyrePage
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






