from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select

try:
    from user_input import User, AppointmentWish

except ModuleNotFoundError:
    from ...main.python.user_input import User, AppointmentWish


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
    # todo: evtl. here if else structure depending on appointment wish district
    # else: (if none or appointment is not available in preferred district)
    elem_berlinweit = browser1.find_element(By.LINK_TEXT, "Termin berlinweit suchen")
    elem_berlinweit.click()


def still_looking_for_appointment(browser1) -> bool:
    termin_search_ongoing = True

    while termin_search_ongoing:
        try:
            # booking appointment if there is one on the 1st calender page
            # todo: select by class "buchbar" instead (that skips available dates for the current day - too soon?)
            # eventually make a list of possible class buchbar elements and filter
            elem_buchen = browser1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
            elem_buchen.click()
            termin_search_ongoing = False
        except NoSuchElementException:
            try:  # if no appointment on calendar page 1: try next calender page
                elem_next = browser1.find_element(By.CSS_SELECTOR, "[title~=nächster]")
                elem_next.click()
                elem_buchen = browser1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
                elem_buchen.click()
                termin_search_ongoing = False
            except NoSuchElementException:
                # todo: evtl. additionally to console print add timestamp to no_dates_available_attempts.csv file
                print("Leider aktuell kein buchbarer Termin vorhanden!"
                      "Neue Suche in den kommenden 24 Stunden beauftragt.")
                break
    return termin_search_ongoing

#
# def book_appointment_2ndpage(browser1, termin_search_ongoing1):
#     """
#     if no appointment on calendar page 1:
#     turn calender page and try next calender page
#
#     :param browser1:
#     :param termin_search_ongoing1:
#     :return: termin_search_ongoing1:
#     """
#     elem_next = browser1.find_element(By.CSS_SELECTOR, "[title~=nächster]")
#     elem_next.click()
#     elem_buchen = browser1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
#     elem_buchen.click()
#     termin_search_ongoing1 = False
#     return termin_search_ongoing1
#
#
# def book_appointment_1stpage(driver1, termin_search_ongoing1):
#     """
#     booking appointment if there is one available on the first calender page
#     :param driver1:
#     :param termin_search_ongoing1:
#     :return: termin_search_ongoing1:
#     """
#     # todo: select by class "buchbar" instead (that skips available dates for the current day - too soon?)
#     # eventually make a list of possible class buchbar elements and filter
#     elem_buchen = driver1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
#     elem_buchen.click()
#     termin_search_ongoing1 = False
#     return termin_search_ongoing1


def select_appment(driver1):
    elem_place_time = driver1.find_elements(By.CSS_SELECTOR, "[title~=Zeitpunkt]")
    # todo: specify time (and place)
    if type(elem_place_time) == list:  # if more than one appointment
        for available_appointment in elem_place_time:
            available_appointment.click()  # click on first appointment
            break
    else:
        elem_place_time.click()


def fill_form_with_personal_info(person1, driver1):
    # automatically input name:
    elem_family_name = driver1.find_element(By.ID, "familyName")
    elem_family_name.send_keys(person1.first_name + " " + person1.last_name)
    # automatically input email address:
    elem_email = driver1.find_element(By.ID, "email")
    elem_email.send_keys(person1.email)
    # automatically select from drop down menu:
    elem_select_eval = Select(
        WebDriverWait(driver1, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "field-type-select"))))
    elem_select_eval.select_by_value('0')

    # agb Checkbox:
    elem_nutzungsbedingungen = driver1.find_element(By.ID, "agbgelesen")  # this is not a typo!
    elem_nutzungsbedingungen.click()


def book_appointment(driver1):
    """
    submits the appointment registration form
    -> DO NOT CAll THIS FUNCTION if you do not really want to book an appointment!!!

    :param driver1:
    :return: -
    """
    btn_termin_eintragen = driver1.find_element(By.ID, "register_submit")
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
