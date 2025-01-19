import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestAmazon(BaseTest):

    def test_automate_amazon(self):
        assert_array = []
        login_page = LoginPage(driver=self.driver, title='amazon login')
        login_page.goto()

        mobile_phone = login_page.test_validate_mobile_search_in_amazon(value='Samsung Galaxy S23 Ultra')
        if mobile_phone != 'Samsung Galaxy S23 Ultra 5G AI Smartphone (Green, 12GB, 256GB Storage)':
            assert_array.append("Mobile phone searched is Not Matching")
        login_page.test_add_to_cart(buying_option=mobile_phone)
        login_page.sign_in_to_amazon_account("Ankit", "9334570538", "Test@1234565")

        assert not assert_array, assert_array





