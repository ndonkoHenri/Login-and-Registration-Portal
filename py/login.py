from kivymd.uix.screen import MDScreen
from kivymd_extensions.sweetalert import SweetAlert


class LoginScreen(MDScreen):
    """
    The Login Screen: for user authentication
    """
    def account_login(self, *args):
        is_email = True if "@" in args[0].text else False

        # Create an alert object to report for the various failures/errors
        error_alert = SweetAlert(font_style_footer="Subtitle2", font_style_text="Subtitle1", font_style_title="H5",
                                 timer=10.5, color_button=[1, 0, 0, .9], text_color_button=[1, 1, 0, 1])
        # Create an alert object to report for the various for successes
        success_alert = SweetAlert(font_style_footer="Subtitle2", font_style_text="Subtitle1",
                                   font_style_title="H4", timer=0,
                                   color_button=(0, 1, 0, .8), text_color_button=(0, 0, 1, 1))

        # check if there is a field with no entry
        for instance in args:
            if not instance.text:
                return error_alert.fire("Field-Error", f"The field {instance._ref_name.rstrip('[sup]*[/sup]')} has no entry!",
                                        "Provide both entries to login!", type="warning")

        if self.check_credentials(args[0].text, args[-1].text, is_email):
            # user recognised by our system...
            self.clear_fields(args)
            return success_alert.fire("Success", f"Happy to see you back {args[0].text}!",
                                      type="success")

        else:
            return error_alert.fire("Account Not Found",
                                    f"Sorry, but your account was not found. Please check your credentials and try again.",
                                    "If you forgot your password, you can reset it.", type="warning")

    def clear_fields(self, *args):
        """
        The clear_fields function clears the text of all the fields of the username, password, and
        verification password input boxes. This happens only when the form is submitted successfully.

        :param *args: All the fields(their instances)
        """
        for instance in args:
            instance.text = ""

    def check_credentials(self, username_or_email: str, pwd: str, is_email: bool) -> bool:
        pass
