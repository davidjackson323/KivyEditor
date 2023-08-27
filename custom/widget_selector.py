from kivy.lang import Builder
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
from kivymd.tools.hotreload.app import MDApp
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


class WidgetSelector(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.testing_manager, 0.1)
        self.manager = MDApp.get_running_app().manager


    def testing_manager(self, *args):
        print(self.manager.widget_list)

        
    