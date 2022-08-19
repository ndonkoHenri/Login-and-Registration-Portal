import json
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.window import Window

# minimum height for the desktop window
Window.minimum_width = 372
Window.minimum_height = 640
# window size at start
Window.size = (372, 640)


class TheManager(MDScreenManager):
    """
    The Screen manager (or Assembler) of the App.
    """

    def __init__(self, **kwargs):
        Builder.load_file('kv/root.kv') # contains the Root Widget, hence loaded before init of our screen manager

        super().__init__(**kwargs)
        Builder.load_file('kv/components.kv')
        Clock.schedule_once(self.add_screens)
        """
        Adding the screens to the Root (ScreenManager).
        """

    def add_screens(self, interval):
        # adds the screens to the screenManager
        """
        If you need to use more screens in your app,
        Create your screen files like below:
            1. Create screen_file.py in the folder named py
            2. Create screen_file.kv in the folder named kv
            3. Add the screen details in screens.json like below:
                {
                    ...,
                    "screen_name": {
                        "import": "from libs.uix.baseclass.screen_py_file import ScreenObject",
                        "kv": "libs/uix/kv/screen_kv_file.kv",
                        "object": "ScreenObject()"
                    }
                }
                Note: In .JSON you must not use:
                        * Unneeded Commas
                        * Comments
        """
        with open("screens.json") as f:
            screens = json.load(f)

        for screen_name in screens.keys():
            screen_details = screens[screen_name]
            Builder.load_file(screen_details["kv"])  # loads the respective kv file
            exec(screen_details["import"])  # excecuting imports
            screen_object = eval(screen_details["object"])  # calling it
            screen_object.name = screen_name  # setting the name of the screen be the key
            self.add_widget(
                screen_object
            )  # finally, adding it to the screen manager
