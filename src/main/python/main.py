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
import sched
import time
import random
import requests
# from bs4 import BeautifulSoup
from user_input import User, AppointmentWish
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import civilservice_bot as bot

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

# todo: check why headless does not work yet
options = Options()
options.headless = True  # headless mode means that the code executes in the background

url = "https://service.berlin.de/terminvereinbarung/"


def create_driver(url1):
    driver1 = webdriver.Firefox()
    driver1.get(url1)
    driver1.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    return driver1


# 3) Scheduler

task_done = False  # scheduler variable
task_scheduler = sched.scheduler(time.time, time.sleep)  # scheduler object


def schedule(url2, personal_info, person_appointment_wish):
    global task_done  # task_done is used globally
    driver = create_driver(url2)  # creates a selenium browser object for the given url
    bot.search_appment_type(person_appointment_wish, driver)  # bot searches appointment types with help of driver and appointment wish
    bot.chose_appment_location(person_appointment_wish, driver)  # bot choses appointment based on wish
    termin_search1: bool = bot.not_found_appment(person_appointment_wish, driver)  # did the bot not find an appointment?
    if not termin_search1:  # bot found an appointment
        bot.select_appment(driver)  # bot selects an appoinment
        bot.fillform_and_book_appment(personal_info, driver)  # bot fills out forms with user information and books appoinment
        driver.quit()  # selenium browser object is shut down
        task_done = True  # to stop the scheduler
    else:
        #  if the bot did not find an appointment:
        #  task is repeated randomly within in the next 24 Hours
        task_scheduler.enter(random.randint(0, 86400), 1, schedule, ())
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

    schedule(url, person, person_app_wish)  # run the scheduled tasks


#     Ari = lib.User.user_input()
#     # print("Ari: ", Ari.first_name)
#
#     result = requests.get("https://service.berlin.de/terminvereinbarung/termin/day/")
#     print(result.status_code)  # 200 OK response indicates that page is present
#     print(result.headers)
#     # create soup object from page content with bs4:
#     soup = BeautifulSoup(result.content, 'html.parser')  # "html.parser" instead of lxml
#     # todo: create a list with all sections of class "buchbar":
#     lists = soup.find_all("section")
#     print(lists)
#     https://www.crummy.com/software/BeautifulSoup/bs4/doc/  (beautiful soup documentation)
