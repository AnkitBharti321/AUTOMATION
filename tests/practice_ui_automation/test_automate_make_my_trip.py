import datetime

from pages.login_page import LoginPage
from tests.base_test import BaseTest
import pytest


class TestAutomateMakeMyTrip(BaseTest):

    def test_validate_flight_make_my_trip(self):
        login_page = LoginPage(driver=self.driver)
        date = datetime.datetime.now()
        months= {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
        login_page.goto()
        login_page.test_close_login_create_account_screen()
        login_page.test_search_flight_source_to_destination(source='From', loc='Mumbai, India')
        login_page.test_search_flight_source_to_destination(source='To', loc='New Delhi, India')
        login_page.test_search_flight_date(day=date.day+1, month=months[date.month], year=date.year)
        a=5

    def test_validate_hotel_make_my_trip(self):
        login_page = LoginPage(driver=self.driver)
        date = datetime.datetime.now()
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                  9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        login_page.goto()
        login_page.test_close_login_create_account_screen()
        login_page.test_go_to_hotel_tab()
        login_page.test_search_hotel(location='Delhi')
        login_page.test_check_in_and_check_out_hotel(day=date.day+2, month=months[date.month], year=date.year)
        login_page.test_check_in_and_check_out_hotel(day=date.day + 3, month=months[date.month], year=date.year)
        login_page.test_select_rooms_and_guests(count_of_children=1, age_of_children=5)
        a = 5



