from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
#from custom.color_selector import ColorSelector
#import color_selector
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"



class WidgetSettings(MDScrollView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(self.ids)#.color_copy.y = 100


    