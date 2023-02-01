import unittest
from unittest.mock import patch
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

try:
    import src.main.python.civilservice_bot

except ModuleNotFoundError:
    from ...main.python.civilservice_bot import search_appment_type

try:
    import src.main.python.user_input

except ModuleNotFoundError:
    from ...main.python.user_input import User, AppointmentWish


# try:
#     import main
#
# except ModuleNotFoundError:
#     from ...main.python.main import *


class AppointmentBotTest(unittest.TestCase):

    # @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

        # navigate to the civil service page
        self.driver.get('https://service.berlin.de/terminvereinbarung')

    def test_search_appment_type(self):
        # check if appointment types exist on page
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Personalausweis beantragen"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Reisepass beantragen"))
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Anmelden einer Wohnung"))

    # def...():
    #     self.browser.get('https://service.berlin.de/terminvereinbarung')
    #     self.assertIn('Google', self.browser.title)

    # # @staticmethod
    # def test_get_url_content(self):
    #     with patch('main.requests.get') as mocked_get:
    #         mocked_get.return_value.ok = True
    #         mocked_get.return_value.text = 'Success'

    # @classmethod
    # to close the browser in the end
    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self, locator_type, locator_value):
        """
        Method to confirm the presence of an element on url-page
        -input: locator_type (selenium element id type)
                locator_value (specific element value to look for)
        """
        try:
            self.driver.find_element(by=locator_type, value=locator_value)
        except NoSuchElementException:
            return False
        return True

# if __name__ == '__main__':
#    unittest.main()
