import pytest

from pages.login_page import LoginPage
from tests.base_test import BaseTest
import json

base_url = "https://gorest.co.in/"
authorization_token = "Bearer 1fa25c8ef2fd8fc11a04ee06bbaeda6fa8d1c95dbd74e6680c32b7a4248b4eb9"


class TestAutomateAPI(BaseTest):

    def test_automate_api(self):
        assert_array = []
        login_page = LoginPage(self.driver)
        # login_page.goto()

# GET
        get_response = login_page.get_request(base_url=base_url, auth_token=authorization_token)
        if get_response != 200:
            assert_array.append("This connection was not successful")


# POST
        post_response = login_page.post_request(base_url=base_url, auth_token=authorization_token)
        if post_response != 201:
            assert_array.append("This connection was not successful")

# PUT
        response_get = login_page.get_request(base_url=base_url, auth_token=authorization_token)
        json_data = get_response.json()
        json_str = json.dumps(json_data, indent=4)
        print("The response is: ", json_str)

        uid = response_get.json()[0]['id']
        put_response = login_page.put_request(base_url=base_url, auth_token=authorization_token, user_id=uid)
        if put_response != 200:
            assert_array.append("This connection was not successful")

# DELETE

        delete_response = login_page.delete_request(base_url=base_url, auth_token=authorization_token, id=uid)
        if delete_response != 204:
            assert_array.append("This connection was not successful")
        a = 5

