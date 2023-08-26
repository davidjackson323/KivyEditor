from kivy.lang import Builder
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


class WidgetSelector(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    
    # def print_attributes(self, *args):
    #     test_layout = MDFloatLayout()
        
    