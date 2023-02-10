from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from src.main.python.decorators import modus_operandi
import requests

try:
    from user_input import UserInfo, AppointmentWish, BotSearchInterval

except ModuleNotFoundError:
    from ...main.python.user_input import UserInfo, AppointmentWish, BotSearchInterval


@modus_operandi
def use_element(browser1, sometext, bytype):
    """
    Helperfunction that finds an element on a website an clicks on it
    :param browser1: selenium webdriver object
    :param sometext: the text to look for
    :param bytype: the element type to search the page for
    :return: -
    """
    return browser1.find_element(bytype, sometext)


def still_looking_for_appointment(browser1, search_interval1: BotSearchInterval) -> bool:
    """
    if appointment dates are not available return True,
    if there is at lest one appointment date available return False.
    :param search_interval1: the user's specified search interval for the bot
    :param browser1: selenium browser object
    :return: -
    """

    while True:
        try:
            # booking appointment if there is one on the 1st calender page
            # choose_app_date(browser1)
            use_element("click", browser1, "[title~=buchen]", By.CSS_SELECTOR)
            return False
        except NoSuchElementException:
            try:  # if no appointment on calendar page 1: try next calender page
                # turn_cal_page(browser1)
                use_element("click", browser1, "[title~=nächster]", By.CSS_SELECTOR)
                use_element("click", browser1, "[title~=buchen]", By.CSS_SELECTOR)
                # choose_app_date(browser1)
                return False
            except NoSuchElementException:
                print("Currently no appointments are available!\n"
                      "New automatic search scheduled in " + str(search_interval1.interval_hours) + " hour(s).\n")
                break
    return True


def select_appment(browser1):
    """
    selects the first available appointment
    :param browser1: selenium browser object
    :return: -
    """
    elem_place_time = browser1.find_elements(By.CSS_SELECTOR, "[title~=Zeitpunkt]")
    if type(elem_place_time) == list:  # if more than one appointment
        for available_appointment in elem_place_time:
            available_appointment.click()  # click on first appointment
            break
    else:
        elem_place_time.click()


def fill_form_with_personal_info(person1: UserInfo, browser1):
    """
    automatically fill personal information into booking form
    :param person1: class that holds the user's personal information
    :param browser1: selenium browser object
    :return:
    """
    # automatically input name:
    elem_family_name = browser1.find_element(By.ID, "familyName")
    elem_family_name.send_keys(person1.first_name + " " + person1.last_name)

    # automatically input email address:
    elem_email = browser1.find_element(By.ID, "email")
    elem_email.send_keys(person1.email)


def use_drop_down_menu(browser1):
    # automatically select from drop down menu:
    elem_select_eval = Select(
        WebDriverWait(browser1, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "field-type-select"))))
    elem_select_eval.select_by_value('0')


def is_page_status_ok(page_html) -> bool:
    """
    checks if the website's information is accessible
    :param page_html: the website's html code
    :return: boolean depending on the status code
    """
    if page_html.status_code != 200:
        print("URL Page Information not accessible")
        return True
    else:
        return False


def get_url_content(browser1):
    """
    returns html of a website if page status is OK
    :param browser1: webdriver object that has the current url
    :return: html code of the url
    """
    page_html = requests.get(browser1.current_url)
    # check if url could not be accessed:
    if is_page_status_ok(browser1.current_url):
        return page_html


if __name__ == "__main__":
    person_app = AppointmentWish()
    person = UserInfo()
    search_interval = BotSearchInterval()
    browser = webdriver.Firefox()
    browser.get("https://service.berlin.de/terminvereinbarung/")
    browser.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    use_element(browser, person_app.appointment_type, By.LINK_TEXT)
    use_element("click", browser, "Termin berlinweit suchen", By.LINK_TEXT)
    termin_search1: bool = still_looking_for_appointment(browser, search_interval)
    select_appment(browser)
    fill_form_with_personal_info(person, browser)
    use_element("click", browser, "agbgelesen", By.ID)
    # !!! submit registered form only incomment when you really want to book an appointment:
    # use_element("click", browser, "register_submit", By.ID)
