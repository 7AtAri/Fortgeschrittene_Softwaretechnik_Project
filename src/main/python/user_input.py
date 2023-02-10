from re import search
from typing import Final
from pyrsistent import pvector


def converter(n):
    """
    Helperfunction to convert measurements
    :param n: int (number to be multiplied with)
    :return: lambda function
    """
    return lambda x: x * n


class UserInfo:
    """
    Relevant information about the UserInfo
    Attributes:
        first name (str)
        last name (str)
        email (str)
    """

    # constructor:
    def __init__(self):
        print("Please enter some information about yourself.")
        while True:
            try:
                fname = input("first name:")
                assert (fname.isalpha())
                assert (len(fname) > 1)
                self.first_name = fname

                lname = input("last name:")
                assert (lname.isalpha())
                assert (len(lname) > 1)
                self.last_name = lname
                break
            except AssertionError:
                print("This is not a valid name. Try again!")

        while True:
            try:
                email_inp = input("email:")
                assert (search(r"\w+@+\w+\.(com|net|de|eu)", email_inp))
                self.email = email_inp
                break
            except AssertionError:
                print("This is not a valid email. Try again!")


class AppointmentWish:
    """
    Relevant information about the appointment
     Attributes:
        - Type of appointment
        - evtl. add Preferred district
        - evtl. add Preferred times
    """

    #  later evtl.
    #  -> improve day, time preferences
    def __init__(self):
        print("Choose type of Appointment:\n"
              "- Reisepass beantragen\n"
              "- Personalausweis beantragen\n"
              "- Anmelden einer Wohnung\n")
        appointments = ["Reisepass beantragen", "Personalausweis beantragen", "Anmelden einer Wohnung"]
        while True:
            try:
                appointment_type = input("Type of Appointment:")
                assert ((appointment_type in appointments) is True)
                self.appointment_type = appointment_type
                print("\n")
                break
            except AssertionError:
                print("This is not a valid appointment type. Try again!")


class BotSearchInterval:
    """
    Relevant information about the search interval.
    Choose within how many hours the bot should
    randomly look again for available appointment options
    Attributes:
        - search interval
    """

    def __init__(self):

        seconds_per_hour: Final[int] = 3600
        min_interval_hours: Final[int] = 1
        max_interval_hours: Final[int] = 72

        convert_hours_to_seconds = converter(seconds_per_hour)

        list_available_hours = pvector([x for x in range(min_interval_hours, max_interval_hours)])

        print("Please choose the preferred search interval,\n"
              "in case there is currently no appointment available.\n"
              "Available options are between 1 and 72 (hours).")

        while True:
            try:
                interval_hours = input("Interval:")
                self.interval_hours = interval_hours
                assert (interval_hours.isnumeric())
                assert ((int(interval_hours) in list_available_hours) is True)
                self.interval_in_seconds = convert_hours_to_seconds(int(interval_hours))
                print("\n")
                break
            except AssertionError:
                print("This is not a valid interval. Try again!")


if __name__ == "__main__":
    a = UserInfo()
    b = AppointmentWish()
    c = BotSearchInterval()
