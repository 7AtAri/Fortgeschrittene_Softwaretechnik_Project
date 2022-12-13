from re import search


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
                assert(search(r"\w+@+\w+\.(com|net|de|eu)", email_inp))
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

    #  todo later evtl.
    #  -> improve day, time preferences
    def __init__(self):
        print("Choose type of Appointment:\n"
              "- Reisepass\n"
              "- Personalauseis\n"
              "- Wohnungsanmeldung\n")
        #     "- Gewerbeanmeldung\n") # Gewerbeanmeldung appointments are not "berlinweit"
        #     - focus on most common appointment wishes
        self.appointment_type = input("Type of Appointment:")
        # todo try and except wrong input

        # print("Choose preferred district office:\n"
        #       "- Charlottenburg-Wilmersdorf\n"
        #       "- Friedrichshain-Kreuzberg\n"
        #       "- Lichtenberg\n"
        #       "- Marzahn-Hellersdorf\n"
        #       "- Mitte\n"
        #       "- Neukölln\n"
        #       "- Pankow\n"
        #       "- Reinickendorf\n"
        #       "- Spandau\n"
        #       "- Steglitz-Zehlendorf\n"
        #       "- Tempelhof-Schöneberg\n"
        #       "- Treptow-Köpenik\n"
        #       "- None")
        # self.preferred_district = input("Preferred district office:")
        # # todo try and except wrong input

        # picking certain days eventually too complicated because only date is in html not weekday
        # print("Choose preferred Weekday:\n"
        #       "- Monday\n"
        #       "- Tuesday\n"
        #       "- Wednesday\n"
        #       "- Thursday\n"
        #       "- Friday\n"
        #       "- None")
        # self.preferred_weekday = input("Preferred weekday:")
        # # todo try and except wrong input

        # print("Choose preferred Daytime:\n"
        #       "- Morning\n"
        #       "- Afternoon\n"
        #       "- None")
        #
        # self.preferred_daytime = input("Preferred Daytime:")
        # # todo try and except wrong input


if __name__ == "__main__":
    a = User()
    b = AppointmentWish()
