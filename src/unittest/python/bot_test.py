import geckodriver_autoinstaller
from pyvirtualdisplay import Display
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

try:
    from src.main.python.civilservice_bot import search_appment_type

except ModuleNotFoundError:
    from ...main.python.civilservice_bot import search_appment_type

try:
    from src.main.python.user_input import UserInfo, AppointmentWish

except ModuleNotFoundError:
    from ...main.python.user_input import UserInfo, AppointmentWish


display = Display(visible=False, size=(800, 800))
display.start()

geckodriver_autoinstaller.install()


class AppointmentBotTest(unittest.TestCase):

    # @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

        # navigate to the civil service page
        self.driver.get('https://service.berlin.de/terminvereinbarung')

    def test_search_appment_type_personalausweis(self):
        # check if appointment type exists on page
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Personalausweis beantragen"))

    def test_search_appment_type_reisepass(self):
        # check if appointment type exists on page
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Reisepass beantragen"))

    def tearDown(self) -> None:
        self.driver.quit()

    def is_element_present(self, locator_type, locator_value):
        """
        Helpermethod to confirm the presence of an element on url-page
        -input: locator_type (selenium element id type)
                locator_value (specific element value to look for)
        """
        try:
            self.driver.find_element(by=locator_type, value=locator_value)
        except NoSuchElementException:
            return False
        return True


if __name__ == '__main__':
    display = Display(visible=False, size=(800, 800))
    display.start()
    geckodriver_autoinstaller.install()
    # chromedriver_autoinstaller.install()
    unittest.main()
