# Ari (Sara) Wahl
# Project :  Terminbuchungs-Bot


""" STEPS:
# 1) User Input
# Name, type of appointment, email-address, optional: preferred day, optional: preferred time, optional: preferred area

# 2) Scheduler?
# -> choose time of execution

# 3 ) Web Scraper
# -> Area
# -> available DATE, TIME

# 4) Bot
# -> choose type of appointment
# -> inserting: email, name
# -> Booking a fitting DATE, TIME
"""

# Load needed libraries:

import requests
from bs4 import BeautifulSoup
from user_input import User, AppointmentWish
from selenium.webdriver.firefox.options import Options

# import datetime #for scheduling
# from civilservice_bot import ...


# 1) User input and class User:
# see user_input.py

person_app = AppointmentWish()
person = User()

# 2) Scheduler

# 3) Web scraper and Automation

# make sure the driver is in your path
# DRIVER_PATH = 'geckodriver'
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)
# all options for selenium with firefox:
# https://www.selenium.dev/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html

options = Options()
options.headless = True  # headless mode means that the code executes in the background

url = "https://service.berlin.de/terminvereinbarung/"


def create_driver(url1):
    driver = webdriver.Firefox()
    driver.get(url1)
    driver.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    return driver


search_appment_type(person_app, driver)
chose_appment_location(person_app, driver)
termin_search1: bool = find_appment(person_app, driver)
if not termin_search1:
    select_appment(driver)
    fillform_and_book_appment(person, driver)


# todo: decide what to keep of the old code:
# obtain content from webpage with request:
def get_url(url1, add_info=None):
    return url1 + str(add_info)


def get_content(url1, add_info=None):
    page_html = requests.get(get_url(url1, add_info))
    # check if url could not be accessed:
    if check_page_status(url1):
        return page_html


def check_page_status(page_html) -> bool:
    if page_html.status_code != 200:
        print("URL Page Information not accessible")
        return true
    else:
        return false


# page_html_out = get_content()
page_html_out = requests.get("https://service.berlin.de/terminvereinbarung/termin/day/")

# create soup object from page content with bs4:
soup = BeautifulSoup(page_html_out.content, 'html.parser')  # "html.parser" instead of lxml

# create a list with all sections of class "buchbar":
lists = soup.find_all("section")
print(lists)

if __name__ == "__main__":
    # Ari = lib.User.user_input()
    # print("Ari: ", Ari.first_name)

    result = requests.get("https://service.berlin.de/terminvereinbarung/termin/day/")
    print(result.status_code)  # 200 OK response indicates that page is present
    print(result.headers)
