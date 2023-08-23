from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

class ColorBox(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ColorSelector(MDRelativeLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_interval(self.update_color_button, 0.05)
        Clock.schedule_interval(self.update_slider_color, 0.05)
        #print(self.ids)#.color_copy.y = 100

    def convert_to_relative(self, *args, red = 0, blue = 0, green = 0, alpha = 1):
        return (red / 255, green / 255, blue / 255, alpha / 255)

    def update_slider_color(self, *args):
        # hint_bg_color: "red"
        # thumb_color_active: 'red'
        # thumb_color_inactive: "red"
        red = self.ids.red_slider.value
        self.ids.red_slider.hint_bg_color = red/255, 0, 0, 1
        self.ids.red_slider.color = red/255, 0, 0, 1

        green = self.ids.green_slider.value
        self.ids.green_slider.hint_bg_color = 0, green/255, 0, 1
        self.ids.green_slider.color = 0, green/255, 0, 1

        blue = self.ids.blue_slider.value
        self.ids.blue_slider.hint_bg_color = 0, 0, blue/255, 1
        self.ids.blue_slider.color = 0, 0, blue/255, 1

        alpha = self.ids.alpha_slider.value
        self.ids.alpha_slider.hint_bg_color = 1, 1, 1, alpha/255
        self.ids.alpha_slider.color = 1, 1, 1, alpha/255

    def copy_color_to(self, *args):

        red = self.ids.red_slider.value
        green = self.ids.green_slider.value
        blue = self.ids.blue_slider.value
        alpha = self.ids.alpha_slider.value
        color_code = self.convert_to_relative(red = red, blue = blue, green = green, alpha = alpha)

    
        root = self.get_root_window()
        root = root.children[0].children[0]
        app_view = root.ids.view_port
        draw_to = app_view.canvas
        draw_to.clear()
        print(red, green, blue, alpha)
        
        color = Color(color_code[0], color_code[1], color_code[2], color_code[3])
        draw_to.before.add(color)

        rectangle = Rectangle(pos = (0, 0), size = app_view.size)
        draw_to.before.add(rectangle)



    def update_color_button(self, *args):
        red = self.ids.red_slider.value
        blue = self.ids.blue_slider.value
        green = self.ids.green_slider.value
        alpha = self.ids.alpha_slider.value

        color_code = self.convert_to_relative(red = red, blue = blue, green = green, alpha = alpha)

        #print('red', red, 'green', green, 'blue', blue, 'alpha', alpha)
        #print('code is ', color_code)
        self.ids.copy_color.md_bg_color = color_code

    def update_slider_position(self, *args, instance = None, slider = None):
        #print('hapenning')
        value = instance.text

        try:
            float(value)
        except:
            value = 0

        value = float(value)

        if value > 255:
            value = 255

        if value < 0:
            value = 0


        if slider == 'red':
            self.ids.red_slider.value = value

        if slider == 'green':
            self.ids.green_slider.value = value

        if slider == 'blue':
            self.ids.blue_slider.value = value

        if slider == 'alpha':
            self.ids.alpha_slider.value = value