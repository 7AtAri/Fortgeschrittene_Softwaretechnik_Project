# Ari (Sara) Wahl
# Project :  Terminbuchungs-Bot


""" STEPS:
# 1) User Input
# Name, type of appointment, email-address, optional: preferred day, optional: preferred time, optional: preferred area

# 2 ) Web Scraper
# -> Area
# -> available DATE, TIME

# 3) Scheduler?
# -> choose time of execution

# 4) Bot
# -> choose type of appointment
# -> inserting: email, name
# -> Booking a fitting DATE, TIME
"""
# Load needed libraries:
import sched
import time
import requests
from user_input import User, AppointmentWish
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import civilservice_bot as bot
import secrets

# 1) User input and class User:
# see user_input.py

person_app_wish = AppointmentWish()
person = User()

# 2) Web scraper and Automation

# Please make sure the driver is in your path
# DRIVER_PATH = 'geckodriver'
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)
# all options for selenium with firefox:
# https://www.selenium.dev/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html

options = Options()
options.headless = True  # headless mode means that the code executes in the background
url = "https://service.berlin.de/terminvereinbarung/"


def create_browser_marionette(url1):
    browser1 = webdriver.Firefox()
    browser1.get(url1)
    browser1.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    return browser1


# 3) Scheduler

task_scheduler1 = sched.scheduler(time.time, time.sleep)  # scheduler object


def schedule(url2, personal_info, person_appointment_wish, task_scheduler):
    browser = create_browser_marionette(url2)  # creates a selenium browser object for the given url
    bot.search_appment_type(person_appointment_wish, browser)  # bot searches appointment types with help of browser and appointment wish
    bot.choose_appment_location(browser)  # bot choses appointment based on wish
    termin_search_ongoing_1: bool = bot.still_looking_for_appointment(browser)  # did the bot not find an appointment?
    if not termin_search_ongoing_1:  # bot found an appointment
        bot.select_appment(browser)
        bot.fill_form_with_personal_info(personal_info, browser)
        bot.book_appointment(browser)
        browser.quit()  # selenium browser object is shut down
    else:
        #  if the bot did not find an appointment:
        #  task is repeated randomly within in the next 24 Hours
        task_scheduler.enter(secrets.randbelow(person_appointment_wish.search_interval_in_seconds), 1, schedule, ())
        task_scheduler.run()


# todo: check if following functions are usefull
def get_url_content(url1):
    page_html = requests.get(url1)
    # check if url could not be accessed:
    if check_page_status(url1):
        return page_html


def check_page_status(page_html) -> bool:
    if page_html.status_code != 200:
        print("URL Page Information not accessible")
        return True
    else:
        return False


if __name__ == "__main__":
    options = Options()
    options.headless = True  # headless mode means that the code executes in the background
    url = "https://service.berlin.de/terminvereinbarung/"
    task_scheduler1 = sched.scheduler(time.time, time.sleep)  # scheduler object
    schedule(url, person, person_app_wish, task_scheduler1)  # run the scheduled tasks
