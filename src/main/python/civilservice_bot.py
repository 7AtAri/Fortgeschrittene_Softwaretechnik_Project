from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from src.main.python.user_input import User, AppointmentWish


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


def search_appment_type(person_app1: AppointmentWish, driver1):
    while True:
        if person_app1.appointment_type == "Personalausweis":
            elem_perso = driver1.find_element(By.LINK_TEXT, "Personalausweis beantragen")
            elem_perso.click()
            break
        elif person_app1.appointment_type == "Reisepass":
            elem_pass = driver1.find_element(By.LINK_TEXT, "Reisepass beantragen")
            elem_pass.click()
            break
        elif person_app1.appointment_type == "Wohnungsanmeldung":
            elem_wohnung = driver1.find_element(By.LINK_TEXT, "Anmelden einer Wohnung")
            elem_wohnung.click()
            break
        else:
            print("Wrong input! Please enter the type of appointment correctly!")


def chose_appment_location(person_app1: AppointmentWish, driver1):
    # todo: evtl. here if else structure depending on appointment wish district
    # else: (if none or appointment is not available in preferred district)
    elem_berlinweit = driver1.find_element(By.LINK_TEXT, "Termin berlinweit suchen")
    elem_berlinweit.click()


def not_found_appment(person_app1: AppointmentWish, driver1) -> bool:
    termin_search = True  # still looking for an appointment?

    while termin_search:
        try:
            # todo: maybe select by class "buchbar" instead (that skips available dates for the current day - too soon?)
            # eventually make a list of possible class buchbar elements and filter
            elem_buchen = driver1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
            elem_buchen.click()
            termin_search = False
            # break  # if appointment date found leave
        except NoSuchElementException:
            try:  # if no appointment on calendar page 1: try next calender page
                elem_next = driver1.find_element(By.CSS_SELECTOR, "[title~=nächster]")
                elem_next.click()
                elem_buchen = driver1.find_element(By.CSS_SELECTOR, "[title~=buchen]")
                elem_buchen.click()
                termin_search = False
                # break  # if appointment date found leave
            except NoSuchElementException:
                # todo: evtl. instead of console print add timestamp to no_dates_available_attempts.csv file
                print("Leider aktuell kein buchbarer Termin vorhanden!"
                      "Neue Suche in den kommenden 24 Stunden beauftragt.")
                break
                # termin_search = True  # not looking for appointment anymore, because no dates are available
    return termin_search


# todo: if return type is false + chose_app is done -> deactivate scheduler, else repeat
# scheduler is still active
# if return type is false: deactivate scheduler

def select_appment(driver1):
    elem_place_time = driver1.find_elements(By.CSS_SELECTOR, "[title~=Zeitpunkt]")
    # todo: specify time (and place)
    if type(elem_place_time) == list:  # if more than one appointment
        for available_appointment in elem_place_time:
            available_appointment.click()  # click on first appointment
            break
    else:
        elem_place_time.click()


def fillform_and_book_appment(person1, driver1):
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
    elem_nutzungsbedingungen = driver1.find_element(By.ID, "agbgelesen")
    elem_nutzungsbedingungen.click()

    # todo: only uncomment in the end - so that no actual appointment is booked every time
    # submit appointment registration:
    # btn_termin_eintragen=driver1.find_element(By.ID, "register_submit")
    # btn_termin_eintrage.click()


if __name__ == "__main__":
    person_app = AppointmentWish()
    person = User()
    driver = webdriver.Firefox()
    driver.get("https://service.berlin.de/terminvereinbarung/")
    driver.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    search_appment_type(person_app, driver)
    chose_appment_location(person_app, driver)
    termin_search1: bool = not_found_appment(person_app, driver)
    select_appment(driver)
    fillform_and_book_appment(person, driver)
