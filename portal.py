import os
import platform

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivymd.app import MDApp

from py.root import TheManager

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"


class IdentificationPortal(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(IdentificationPortal, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        # set the title of the window to reflect the project
        self.title = "Identification Portal"

        """
        # palette attributes: primary color, secondary_color.. etc Uncomment and change according to your project
        
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"
        self.theme_cls.theme_style = "Dark" 
        """

    def build(self):
        LabelBase.register("JetBrainsMono",
                           fn_regular=os.path.join("assets", "fonts", "JetBrainsMono", "JetBrainsMono-Regular.ttf"),
                           fn_italic=os.path.join("assets", "fonts", "JetBrainsMono", "JetBrainsMono-Italic.ttf"),
                           fn_bold=os.path.join("assets", "fonts", "JetBrainsMono", "JetBrainsMono-Bold.ttf"),
                           fn_bolditalic=os.path.join("assets", "fonts", "JetBrainsMono",
                                                      "JetBrainsMono-Bold-Italic.ttf")
                           )
        return TheManager()

    def register_new_font(self, font_name, location):
        # TODO: make this function work
        pass
