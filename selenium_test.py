import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from lib import User, AppointmentWish

# selenium docu:
# selenium documentation:
# https://selenium-python.readthedocs.io/index.html

# depending on version of selenium, geckodriver is not necessary to use firefox:
# this is the path on my computer where I store the geckodriver for firefox
# os.environ['PATH'] += r"/Users/ari/Documents/Data_Science/1_Semester/Fortgeschrittene\ " \
#                       r"Softwaretechnik/Fortgeschrittene_Softwaretechnik_Project2 "

# css selectors:
# https://www.w3schools.com/cssref/css_selectors.php

# todo: this happens in main
person_app = AppointmentWish()
person = User()

driver = webdriver.Firefox()
driver.get("https://service.berlin.de/terminvereinbarung/")
driver.implicitly_wait(3)

# todo: define function/functions for process below:
while True:
    if person_app.appointment_type == "Personalausweis":
        elem_perso = driver.find_element(By.LINK_TEXT, "Personalausweis beantragen")
        elem_perso.click()
        break
    elif person_app.appointment_type == "Reisepass":
        elem_pass = driver.find_element(By.LINK_TEXT, "Reisepass beantragen")
        elem_pass.click()
        break
    elif person_app.appointment_type == "Wohnungsanmeldung":
        elem_wohnung = driver.find_element(By.LINK_TEXT, "Anmelden einer Wohnung")
        elem_wohnung.click()
        break
    else:
        print("Wrong input! Please enter the type of appointment correctly!")

elem_berlinweit = driver.find_element(By.LINK_TEXT, "Termin berlinweit suchen")
elem_berlinweit.click()

# btn_buchen = []
termin_search = True  # still looking for an appointment?

# todo: improve execpt statements (distinguish expected from unexpected errors)
while termin_search:
    try:
        # todo: maybe select by class "buchbar" instead (that skips available dates for the current day - too soon?)
        # eventually make a list of possible class buchbar elements and filter
        elem_buchen = driver.find_element(By.CSS_SELECTOR, "[title~=buchen]")
        elem_buchen.click()
        break  # if appointment date found leave
    except:
        try:  # if no appointment on calendar page 1: try next calender page
            elem_next = driver.find_element(By.CSS_SELECTOR, "[title~=nächster]")
            elem_next.click()
            elem_buchen = driver.find_element(By.CSS_SELECTOR, "[title~=buchen]")
            elem_buchen.click()
            break  # if appointment date found leave
        except:
            print('Leider kein buchbarer Termin vorhanden')
            termin_search = False  # not looking for appointment anymore, because no dates are available

if termin_search:
    elem_place_time = driver.find_elements(By.CSS_SELECTOR, "[title~=Zeitpunkt]")
    # todo: specify time and place
    if type(elem_place_time) == list:  # if more than one appointment
        for available_appointment in elem_place_time:
            available_appointment.click()  # click on first appointment
            break
    else:
        elem_place_time.click()

# todo -> make function:
# automatically input name:
elem_family_name = driver.find_element(By.ID, "familyName")
elem_family_name.send_keys(person.first_name + " " + person.last_name)
# automatically input email address:
elem_email = driver.find_element(By.ID, "email")
elem_email.send_keys(person.email)
# automatically select from drop down menu:
elem_select_eval = Select(WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "field-type-select"))))
elem_select_eval.select_by_value('0')

# agb Checkbox:
elem_nutzungsbedingungen = driver.find_element(By.ID, "agbgelesen")
elem_nutzungsbedingungen.click()

# todo: only uncomment in the end - so that no actual appointment is booked every time
# submit appointment registration:
# btn_termin_eintragen=driver.find_element(By.ID, "register_submit")
# btn_termin_eintrage.click()


# if __name__ == "__main__":
#     browser = webdriver.Firefox()
#     browser.get('http://selenium.dev/')
