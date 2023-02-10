import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import unittest
# from unittest.mock import patch
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

try:
    from civilservice_bot import search_appment_type
    # import src.main.python.civilservice_bot

except ModuleNotFoundError:
    from ...main.python.civilservice_bot import search_appment_type

try:
    from user_input import User, AppointmentWish
    # import src.main.python.user_input

except ModuleNotFoundError:
    from ...main.python.user_input import User, AppointmentWish


display = Display(visible=False, size=(800, 800))
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
# and if it doesn't exist, download it automatically,
# then add chromedriver to path

chrome_options = webdriver.chrome.options.Options()
# Add your options as needed
options = [
    # Define window size here
    "--window-size=1200,1200",
    "--ignore-certificate-errors"
    # "--headless",
    # "--disable-gpu",
    # "--window-size=1920,1200",
    # "--ignore-certificate-errors",
    # "--disable-extensions",
    # "--no-sandbox",
    # "--disable-dev-shm-usage",
    # '--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)


class AppointmentBotTest(unittest.TestCase):

    # @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(5)

        # navigate to the civil service page
        self.driver.get('https://service.berlin.de/terminvereinbarung')

    def test_search_appment_type_personalausweis(self):
        # check if appointment type exists on page
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Personalausweis beantragen"))

    def test_search_appment_type_reisepass(self):
        # check if appointment type exists on page
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Reisepass beantragen"))

    def test_search_appment_type_anmeldung(self):
        # check if appointment type exists on page
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


if __name__ == '__main__':
    unittest.main()
