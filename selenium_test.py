import os
from selenium import webdriver
from selenium.webdriver.common.by import By
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

person_app = AppointmentWish()

driver = webdriver.Firefox()
driver.get("https://service.berlin.de/terminvereinbarung/")
driver.implicitly_wait(4)

# TODO: distinguish type of appointment
# for now only "Personalausweis beantragen" is possible

while True:
    if person_app.appointment_type == "Personalausweis":
        element_1 = driver.find_element(By.LINK_TEXT, "Personalausweis beantragen")
        element_1.click()
        break
    elif person_app.appointment_type == "Reisepass":
        element_1 = driver.find_element(By.LINK_TEXT, "Reisepass beantragen")
        element_1.click()
        break
    elif person_app.appointment_type == "Wohnungsanmeldung":
        element_1 = driver.find_element(By.LINK_TEXT, "Anmelden einer Wohnung")
        element_1.click()
        break
    else:
        print("Wrong input! Please enter the type of appointment correctly!")

element_2 = driver.find_element(By.LINK_TEXT, "Termin berlinweit suchen")
element_2.click()

element_3 = []
termin_search = True

while termin_search:
    try:
        element_3 = driver.find_element(By.CSS_SELECTOR, "[title~=buchen]")
        termin_search = False
    except:
        try:
            element_4 = driver.find_element(By.CSS_SELECTOR, "[title~=nächster]")
            element_4.click()
            element_3 = driver.find_element(By.CSS_SELECTOR, "[title~=buchen]")
            # print("el3:", element_3)
            element_3.click()
        except: # specify for expected and unexpected error?
            print('Leider kein buchbarer Termin vorhanden')
            termin_search = False

if termin_search:
    element_5 = driver.find_elements(By.CSS_SELECTOR, "[title~=eintragen...]")
# for element in element_5:
# if preferred_borough

# if __name__ == "__main__":
#     browser = webdriver.Firefox()
#     browser.get('http://selenium.dev/')
#     print("el3:", element_3)
