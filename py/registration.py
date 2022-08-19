import string
from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert


class RegistrationScreen(MDScreen):

    def create_account(self, *args):
        """
        Creates an account for the user and displays an Alert with a message(success or error).
        It takes in a list of arguments and checks if there is a field with no entry,
        if the entered texts are less than the imposed max_length(20),
        if the two entered passwords do not match, if password is weak or not and finally
        if checkbox was checked. If all these conditions are met then it creates an account.

        :param *args: All the Fields(their instances)
        :return: An alert accounting for the successful/eroorful creation of the account
        """

        # boolean value to know if everything was successful
        is_success = False

        # Create an alert object to report for the various failures/errors
        error_alert = SweetAlert(font_style_footer="Subtitle2", font_style_text="Subtitle1", font_style_title="H5",
                                 timer=10.5, color_button=[1, 0, 0, .9], text_color_button=[1, 1, 0, 1])

        # check if there is a field with no entry
        for instance in args:
            if not instance.text:
                return error_alert.fire("Field-Error", f"The field {instance._ref_name.rstrip('[sup]*[/sup]')} has no entry!",
                                        "All the fields are required to create an account!", type="warning", )

        # check if the entered texts are less than the imposed max_length(20)
        for instance in args:
            if instance.error:
                return error_alert.fire("Max-Length-Error",
                                        f"The maximum length of {instance._ref_name.rstrip('[sup]*[/sup]')} was exceeded!",
                                        "For security reasons max_length = 20.",
                                        type="warning")

        # Password match check and alert
        if args[-1].text != args[-2].text:
            return error_alert.fire("Password-Match", "The two given passwords do not match!",
                                    "Try using the 'show' option to check if both match before submitting.",
                                    type="warning")

        # verifies if the password meets all the required security measures
        if not self.is_strong_password(args[-1].text):
            return error_alert.fire("Weak Password",
                                    "Password must be minimum 7 characters long and contain at least one digit, lowercase letter, uppercase letter and special character",
                                    "Let's give hackers a hard time!",
                                    type="warning")

        # verifies if the checkbox was checked
        if not self.ids.checkbox.active:
            return error_alert.fire("Terms and Policy",
                                    "Please you must accept our Terms and Privacy Policy to create an acoount!",
                                    "Remember to read before accepting!",
                                    type="warning")
        # if this point is reached, then there was no error! we then account for the success...
        is_success = True
        if is_success:
            # Create an alert object to report for the various for successes
            success_alert = SweetAlert(font_style_footer="Subtitle2", font_style_text="Subtitle1",
                                       font_style_title="H4", timer=0,
                                       color_button=(0, 1, 0, .8), text_color_button=(0, 0, 1, 1))
            self.clear_fields(args)
            return success_alert.fire("Success", f"Your account was successfully created!",
                                      type="success")

    def clear_fields(self, *args):
        """
        The clear_fields function clears the text of all the fields of the username, password, and
        verification password input boxes. This happens only when the form is submitted successfully.

        :param *args: All the fields(their instances)
        """
        for instance in args:
            instance.text = ""

    def is_strong_password(self, pwd) -> bool:
        """
        Checks if the password is strong or not.
        It does this by checking for:
            1) length >= 7 characters,
            2) lowercase character,
            3) uppercase character,
            4) digit and
            5) special character.

        :param pwd: the password entered by the user
        :return: True if the password is at least 7 characters long and contains at least one lowercase letter,
        uppercase letter, digit and special character
        """
        l, u, sc, d = 0, 0, 0, 0
        if len(pwd) >= 7:
            for i in pwd:

                # counting lowercase alphabets
                if i.islower():
                    l += 1

                    # counting uppercase alphabets
                if i.isupper():
                    u += 1

                    # counting digits
                if i.isdigit():
                    d += 1

                # counting the mentioned special characters
                if i in set(string.punctuation):
                    sc += 1
            if l >= 1 and u >= 1 and sc >= 1 and d >= 1 and (l + sc + u + d) == len(pwd):
                return True
            else:
                return False
        else:
            return False