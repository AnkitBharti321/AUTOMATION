from pages.login_page import LoginPage


def test_automate_iphone_names_flipkart(self):
    login_page = LoginPage(self.driver)
    base_page = BasePage(self.driver)
    login_page.goto()
    driver.get("https://www.flipkart.com/")
    search_product = driver.find_element_by_xpath("//input[@name='q']")
    search_product.send_keys("iphone")



