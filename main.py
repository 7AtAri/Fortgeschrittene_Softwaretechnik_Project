# Ari (Sara) Wahl
# Project :  Terminbuchungs-Bot


""" TODO:
# 1) User Input
# Name, type of appointment, email-address, optional: preferred day, optional: preferred time, optional: preferred area

# 2) Scheduler?
# -> choose time of execution

# 3 ) Web Scraper
# -> Area
# -> available DATE, TIME

# 4) Bot
# -> choose type of appointment
# -> Booking of first fitting DATE, TIME
# -> inserting: email, name


"""

# Load needed libraries:

import requests
from bs4 import BeautifulSoup


# import datetime #for scheduling

# 1) User input and class User:
# see lib.py

# 2) Scheduler

# 3) Web scraper

# obtain content from webpage with request:
def get_url(add_info=None):
    return "https://service.berlin.de/terminvereinbarung/" + str(add_info)


def get_content(add_info=None):
    url = get_url(add_info=None)
    page_html = requests.get(get_url())

    # check if url could not be accessed:
    if page_html.status_code != 200:
        print("URL Page Information not accessible")
        return
    return page_html


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
