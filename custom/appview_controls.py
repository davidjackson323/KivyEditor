from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.scatter import Scatter
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"



class AppViewControls(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_size, 0.25)
        Clock.schedule_once(self.set_size_dimensions, 0.25)
        Window.bind(on_resize = self.set_size)

    def set_size(self, *args):
        root = self.get_root_window()
        if root != None:
            root = root.children[0].children[0]
            #print(root.ids)
            full_width = Window.width
            widgets_width = root.ids.widget_selector.width
            settings_width = root.ids.widget_settings.width
            #print("ALL", full_width, widgets_width, settings_width)

            self.size_hint = (None, 0.05)
            self.width = full_width - widgets_width - settings_width
            self.pos_hint_x = None
            self.x = widgets_width
            #print(Window.size)

    def set_size_dimensions(self, *args):
        x_start = self.ids.rotation_controls.width
        print(x_start)

