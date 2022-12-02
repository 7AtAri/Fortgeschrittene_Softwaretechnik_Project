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
        self.first_name = input("first name:")
        self.last_name = input("last name:")
        self.email = input("email:")

    # @classmethod
    # def user_input(self):
    #     # todo: validate input
    #     while True:
    #         first_name = input("First Name: ")
    #         if first_name == bool(""):
    #             print("Enter your Name please!")
    #             continue
    #         last_name = input("Last Name: ")
    #         # todo: assert(...@...):
    #         email = input("E-Mail: ")
    #         try:
    #             return self(first_name, last_name, email)
    #         except:
    #             print("Only Letters please!")
    #             continue

    # @property
    # ...eventually add getter and setter via property decorator


class AppointmentWish:
    """
    Relevant information about the appointment
     Attributes:
        - Type of Appointment
        - Preferred Borough
        - Preferred Times
    """

    #  todo later evtl.
    #  -> improve day, time preferences

    def __init__(self):
        print("Choose type of Appointment:\n"
              "- Reisepass\n"
              "- Personalauseis\n"
              "- Wohnungsanmeldung\n")
        #     "- Gewerbeanmeldung\n")
        self.appointment_type = input("Type of Appointment:")
        # todo try and except wrong input

        print("Choose preferred district office:\n"
              "- Charlottenburg-Wilmersdorf\n"
              "- Friedrichshain-Kreuzberg\n"
              "- Lichtenberg\n"
              "- Marzahn-Hellersdorf\n"
              "- Mitte\n"
              "- Neukölln\n"
              "- Pankow\n"
              "- Reinickendorf\n"
              "- Spandau\n"
              "- Steglitz-Zehlendorf\n"
              "- Tempelhof-Schöneberg\n"
              "- Treptow-Köpenik\n"
              "- None")
        self.preferred_borough = input("Preferred district office:")
        # todo try and except wrong input

        print("Choose preferred Weekday:\n"
              "- Monday\n"
              "- Tuesday\n"
              "- Wednesday\n"
              "- Thursday\n"
              "- Friday\n"
              "- None")
        self.preferred_weekday = input("Preferred weekday:")
        # todo try and except wrong input

        print("Choose preferred Daytime:\n"
              "- Morning\n"
              "- Afternoon\n"
              "- None")

        self.preferred_daytime = input("Preferred Daytime:")
        # todo try and except wrong input


if __name__ == "__main__":
    a = User()
    b = AppointmentWish()
