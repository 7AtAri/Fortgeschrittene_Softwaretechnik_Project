# Ari (Sara) Wahl
# Project :  Terminbuchungs-Bot


""" STEPS:
# 1) UserInfo Input
# Name, type of appointment, email-address,
# optional: preferred day, optional: preferred time, optional: preferred area

# 2 ) Web Scraper
# -> Area
# -> available DATE, TIME

# 3) Scheduler?
# -> choose time of execution

# 4) Bot
# -> choose type of appointment
# -> inserting: email, name
# -> Booking a fitting DATE, TIME

# Please make sure the driver is in your path
# DRIVER_PATH = 'geckodriver'
# driver = webdriver.Firefox(executable_path=DRIVER_PATH)
# all options for selenium with firefox:
# https://www.selenium.dev/selenium/docs/api/py/webdriver_firefox/selenium.webdriver.firefox.options.html
"""
# Load needed libraries:
import sched
import time
from user_input import UserInfo, AppointmentWish, BotSearchInterval
from selenium import webdriver
from selenium.webdriver.common.by import By
import civilservice_bot as bot
import secrets


def create_browser_marionette(url1):
    """
    creates a marionette object of your browser for the bot
    :param url1: url-webaddress
    :return: browser object
    """
    browser1 = webdriver.Firefox()
    browser1.get(url1)
    browser1.implicitly_wait(3)  # webdriver object now waits 3 seconds between each call
    return browser1


def schedule(user_info1, appointment_wish1, bot_search_interval1):
    """
    Schedules the task until it is done
    :param user_info1: user input of personal information for the booking
    :param appointment_wish1: user input of appointment wishes
    :param bot_search_interval1: user input of search interval for the bot
    :return:
    """
    url = "https://service.berlin.de/terminvereinbarung/"

    # creates a selenium browser object for the given url:
    browser = create_browser_marionette(url)

    # bot selects appointment type according to wish:
    bot.use_element("click", browser, appointment_wish1.appointment_type, By.LINK_TEXT)

    # bot selects appointments all over Berlin:
    bot.use_element("click", browser, "Termin berlinweit suchen", By.LINK_TEXT)

    termin_search_ongoing_1: bool = bot.still_looking_for_appointment(browser,
                                                                      bot_search_interval1)  # did the bot not find an appointment?
    if not termin_search_ongoing_1:  # bot found an appointment
        bot.select_appment(browser)
        bot.fill_form_with_personal_info(user_info1, browser)
        bot.use_drop_down_menu(browser)

        # bot checks "AgB gelesen" Box:
        bot.use_element("click", browser, "agbgelesen", By.ID)

        # bot submits the appointment registration:
        # !!! out comment if you don't really want to book an appointment:
        bot.use_element("click", browser, "register_submit", By.ID)

        browser.quit()  # selenium browser object is shut down
    else:
        #  if the bot did not find an appointment:
        #  task is repeated randomly within in the chosen interval
        task_scheduler = sched.scheduler(time.time, time.sleep)  # scheduler object
        search_schedule = task_scheduler.enter(delay=secrets.randbelow(
            bot_search_interval1.interval_in_seconds),
            priority=1,
            action=schedule,
            argument=(user_info1,
                      appointment_wish1,
                      bot_search_interval1))
        task_scheduler.run(blocking=False)
        cancel = input("To cancel the search enter 'cancel': ")
        if cancel:
            task_scheduler.cancel(search_schedule)
            browser.quit()  # selenium browser object is shut down


if __name__ == "__main__":
    schedule(UserInfo(), AppointmentWish(), BotSearchInterval())  # run the scheduled tasks
