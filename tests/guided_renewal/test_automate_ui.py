import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestAmazon(BaseTest):

    def test_automate_amazon(self):
        assert_array = []
        login_page = LoginPage(driver=self.driver, title='amazon login')
        login_page.goto()
        mobile_phone = login_page.test_validate_mobile_search_in_amazon(value='iphone 2024 new model')
        if mobile_phone != 'iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; White':
            assert_array.append("Not Matched")
        login_page.test_add_to_cart(buying_option=mobile_phone)

        assert not assert_array, assert_array





