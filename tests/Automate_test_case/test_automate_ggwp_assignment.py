import pytest
from faker.proxy import Faker

from pages.demo_web_page.demo_web_dashboard_page import DemoWebDashboardPage
from pages.login_page import LoginPage
from tests.base_test import BaseTest


class TestWebDemoWebShop(BaseTest):

    def test_automate_demo_web_shop(self):
        assert_array = []
        faker = Faker()
        # creating objects for page class
        login_page = LoginPage(driver=self.driver, title='Demo web shop login')
        demo_web_dashboard_page = DemoWebDashboardPage(self.driver)
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()
        password = faker.password()
        # Redirecting to the website
        login_page.goto()
        # Registering the account
        demo_web_dashboard_page.register_account_to_demo_web_dashboard_page(value="Register", gender='female',
                                                                            first_name=first_name,
                                                                            last_name=last_name, email=email,
                                                                            password=password)
        # validating the registration message
        if demo_web_dashboard_page.get_complete_registration_confimation_message() != "Your registration completed":
            assert_array.append("Registration confirmation message not displayed")

        demo_web_dashboard_page.click_continue_button()
        if not demo_web_dashboard_page.check_welcome_message_displayed("Welcome to our store"):
            assert_array.append("Welcome message is not displayed")

        # Log out
        demo_web_dashboard_page.click_header_options(options='Log out')

        demo_web_dashboard_page.click_header_options(options='Log in')
        demo_web_dashboard_page.click_register_button()
        # Trying to register again with same email.
        demo_web_dashboard_page.register_account_to_demo_web_dashboard_page(value="Register", gender='female',
                                                                            first_name=faker.first_name(),
                                                                            last_name=faker.last_name(), email=email,
                                                                            password=password)
        # Ensure it throws error upon trying to register with same email
        same_user_error_message = demo_web_dashboard_page.get_registration_error_message()
        if same_user_error_message != 'The specified email already exists':
            assert_array.append("Test failed...Registered emails shouldn't be allowed")

        # Log in with the created user
        demo_web_dashboard_page.click_header_options(options='Log in')

        demo_web_dashboard_page.login_as_user(email=email, password=password)

        # Ensure user is logged successfully
        if email != demo_web_dashboard_page.get_logged_user_account_details():
            assert_array.append("Logged user details are displaying properly")

        # taking the survey community poll
        demo_web_dashboard_page.take_survey_community_poll(option='Good')

        # verifying the poll Results
        poll_results = demo_web_dashboard_page.get_poll_results()
        if not poll_results:
            assert_array.append("poll results are not displayed")

        # Adding a product through dashboard
        product_details =demo_web_dashboard_page.add_products_from_dashboard_page(product = "$25 Virtual Gift Card")
        print(product_details)

        # Asserting the values if the product details are not displayed
        if not product_details:
            assert_array.append("product details are not displayed")

        # Ensure the Name and emails should be prefilled.
        prefilled_value = demo_web_dashboard_page.get_prefilled_name_and_email_address()
        print(prefilled_value)
        if not prefilled_value:
            assert_array.append("Name and email are not prefilled")

        # validating add to cart button without filling recipient name and email.
        demo_web_dashboard_page.add_to_cart_in_product_page()

        error_message_while_adding_product = demo_web_dashboard_page.get_error_message_while_adding_product()
        print(error_message_while_adding_product)

        if not error_message_while_adding_product:
            assert_array.append(error_message_while_adding_product)

        # filling recipient name and email.
        demo_web_dashboard_page.fill_recipient_name_and_email_address(recipient_name=faker.name(), recipient_email=faker.email(), message="Thankyou for being so awesome... you are amazing!!!", quantity=7)

        error_message_upon_click_add_to_cart = demo_web_dashboard_page.get_error_message_while_adding_product()

        if '  The maximum quantity allowed for purchase is 5.' not in error_message_upon_click_add_to_cart:
            assert_array.append("maximum quantity error is being thrown")

        assert not assert_array, assert_array






