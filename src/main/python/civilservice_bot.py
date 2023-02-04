from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

try:
    from user_input import User, AppointmentWish, AppointmentSearchInterval

except ModuleNotFoundError:
    from ...main.python.user_input import User, AppointmentWish, AppointmentSearchInterval


# selenium docu:
# selenium documentation:
# https://selenium-python.readthedocs.io/index.html
# https://www.scrapingbee.com/blog/selenium-python/

# depending on version of selenium, geckodriver is not necessary to use firefox:
# this is the path on my computer where I store the geckodriver for firefox
# os.environ['PATH'] += r"/Users/ari/Documents/Data_Science/1_Semester/Fortgeschrittene\ " \
#                       r"Softwaretechnik/Fortgeschrittene_Softwaretechnik_Project2 "

# css selectors:
# https://www.w3schools.com/cssref/css_selectors.php


def search_appment_type(person_app1: AppointmentWish, browser1):
    """
    Searches for the user's chosen appointment type and selects it
    :param person_app1:
    :param browser1:
    :return:
    """
    while True:
        if person_app1.appointment_type == "Personalausweis":
            elem_perso = browser1.find_element(By.LINK_TEXT, "Personalausweis beantragen")
            elem_perso.click()
            break
        elif person_app1.appointment_type == "Reisepass":
            elem_pass = browser1.find_element(By.LINK_TEXT, "Reisepass beantragen")
            elem_pass.click()
            break
        elif person_app1.appointment_type == "Wohnungsanmeldung":
            elem_wohnung = browser1.find_element(By.LINK_TEXT, "Anmelden einer Wohnung")
            elem_wohnung.click()
            break
        else:
            print("Wrong input! Please enter the type of appointment correctly!")


def choose_appment_location(browser1):
    """
    Chooses all available appointment locations in berlin
    :param browser1:
    :return: -
    """
    elem_berlinweit = browser1.find_element(By.LINK_TEXT, "Termin berlinweit suchen")
    elem_berlinweit.click()


def choose_app_date(browser1):
    elem_buchen = browser1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
    elem_buchen.click()


def turn_cal_page(browser1):
    elem_next = browser1.find_element(By.CSS_SELECTOR, "[title~=nächster]")
    elem_next.click()


def still_looking_for_appointment(browser1, search_interval1: AppointmentSearchInterval) -> bool:
    """
    if appointment dates are not available return True,
    if there is at lest one appointment date available return False.
    :param search_interval1:
    :param browser1:
    :return:
    """
    termin_search_ongoing = True

    while termin_search_ongoing:
        try:
            # booking appointment if there is one on the 1st calender page
            choose_app_date(browser1)
            termin_search_ongoing = False
        except NoSuchElementException:
            try:  # if no appointment on calendar page 1: try next calender page
                turn_cal_page(browser1)
                choose_app_date(browser1)
                termin_search_ongoing = False
            except NoSuchElementException:
                print("Leider aktuell kein buchbarer Termin vorhanden!"
                      "Neue Suche in den kommenden" + str(search_interval1.interval_in_seconds) + " beauftragt.")
                break
    return termin_search_ongoing


def select_appment(browser1):
    """
    selects the first available appointment
    :param browser1:
    :return:
    """
    elem_place_time = browser1.find_elements(By.CSS_SELECTOR, "[title~=Zeitpunkt]")
    # todo: specify time (and place)
    if type(elem_place_time) == list:  # if more than one appointment
        for available_appointment in elem_place_time:
            available_appointment.click()  # click on first appointment
            break
    else:
        elem_place_time.click()


def fill_form_with_personal_info(person1: User, browser1):
    """
    automatically fill personal information into booking form
    :param person1:
    :param browser1:
    :return:
    """
    # automatically input name:
    elem_family_name = browser1.find_element(By.ID, "familyName")
    elem_family_name.send_keys(person1.first_name + " " + person1.last_name)
    # automatically input email address:
    elem_email = browser1.find_element(By.ID, "email")
    elem_email.send_keys(person1.email)
    # automatically select from drop down menu:
    elem_select_eval = Select(
        WebDriverWait(browser1, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "field-type-select"))))
    elem_select_eval.select_by_value('0')

    # agb Checkbox:
    elem_nutzungsbedingungen = browser1.find_element(By.ID, "agbgelesen")  # this is not a typo!
    elem_nutzungsbedingungen.click()


def book_appointment(browser1):
    """
    submits the appointment registration form
    -> DO NOT CAll THIS FUNCTION if you do not really want to book an appointment!!!

    :param browser1:
    :return: -
    """
    btn_termin_eintragen = browser1.find_element(By.ID, "register_submit")
    btn_termin_eintragen.click()


if __name__ == "__main__":
    person_app = AppointmentWish()
    person = User()
    driver = webdriver.Firefox()
    driver.get("https://service.berlin.de/terminvereinbarung/")
    driver.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    search_appment_type(person_app, driver)
    choose_appment_location(driver)
    termin_search1: bool = still_looking_for_appointment(driver)
    select_appment(driver)
    # fill_form_with_personal_info(person, driver)
