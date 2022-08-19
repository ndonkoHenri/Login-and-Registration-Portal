from portal import IdentificationPortal
import traceback  # NOQA: E402

from kivy.factory import Factory  # NOQA: E402
# from kivy.logger import LOG_LEVELS, Logger  # NOQA: E402
# Logger.setLevel(LOG_LEVELS["debug"])

# app version
__version__ = "1.0.0"

# from kivy.core.window import Window
# Window.minimum_width = 372
# Window.minimum_width = 632
# Window.size = (372, 632)


try:
    IdentificationPortal().run()
except Exception:
    error = traceback.format_exc()

    """
    If the app encounters an error it automatically saves the
    error in a file called ERROR.log.
    You can use this for BugReport purposes.
    """
    with open("ERROR.log", "w") as error_file:
        error_file.write(error)

    print(error)
    
    
