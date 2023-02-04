from re import search
from typing import Final


class User:
    """
    Relevant information about the User
    Attributes:
        first name (str)
        last name (str)
        email (str)
    """

    # constructor:
    def __init__(self):
        print("please enter some information about yourself.")
        while True:
            try:
                fname = input("first name:")
                assert (fname.isalpha())
                # assert(len(fname) > 1)
                self.first_name = fname

                lname = input("last name:")
                assert (lname.isalpha())
                # assert(len(fname) > 1)
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
        - evtl. Preferred district
        - evtl. Preferred times
    """

    #  later evtl.
    #  -> improve day, time preferences
    def __init__(self):
        print("Choose type of Appointment:\n"
              "- Reisepass\n"
              "- Personalauseis\n"
              "- Wohnungsanmeldung\n")
        appointments = ["Reisepass", "Personalausweis", "Wohungsanmeldung"]
        while True:
            try:
                appointment_type = input("Type of Appointment:")
                assert ((appointment_type in appointments) is True)
                self.appointment_type = appointment_type
                print("\n")
                break
            except AssertionError:
                print("This is not a valid appoinment type. Try again!")


class AppointmentSearchInterval:
    """
    Relevant information about the search interval.
    Choose within how many hours the bot should
    randomly look again for available appointment options
    Attributes:
        - search interval
    """

    def __init__(self):

        seconds_per_hour: Final[int] = 360
        min_interval_hours: Final[int] = 1
        max_interval_hours: Final[int] = 72

        print("Please choose the preferred search interval,\n"
              "in case there is currently no appointment available.\n"
              "Available options are between 1 and 72 (hours).")

        list_available_hours = [x for x in range(min_interval_hours, max_interval_hours)]
        while True:
            try:
                interval_hours = input("Interval:")
                assert (interval_hours.isnumeric())
                assert ((int(interval_hours) in list_available_hours) is True)
                self.search_interval_in_seconds = int(interval_hours) * seconds_per_hour
                print("\n")
                break
            except AssertionError:
                print("This is not a valid interval. Try again!")


if __name__ == "__main__":
    # a = User()
    b = AppointmentWish()
