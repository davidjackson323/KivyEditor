'''
Ran into issues with Scatter/Scatter Layout that lead to development of t
this app_view code. 

'''

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



class AppView(ScatterLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.set_size)
        Clock.schedule_once(self.draw_grid)


    def set_size(self, *args,  height = None, width = None):
        root = self.get_root_window().children[0].children[0]

        if (height == None) & (width == None):
            print('First Run, setting to max height')
            center = Window.center
            menu_height = root.ids.menu_bar.height
            height = (Window.height - menu_height) * 1
            width = Window.height
            size = width, height
            self.size = size
            #self.scale = scale
            self.auto_center()

            
        else:
            print('setting custom size')
            print(width, height)
            center = Window.center
            menu_height = root.ids.menu_bar.height
            size = width, height
            self.size = size
            #self.scale = scale
            self.auto_center()


    def rotation_allowed(self, *args):
        print(self.do_rotation)
        if self.do_rotation == True:
            self.do_rotation = False

        else:
            self.do_rotation = True
            

    def auto_center(self, *args):
        root = self.get_root_window().children[0].children[0]
        center = Window.center
        menu_height = root.ids.menu_bar.height
        self.pos = (center[0] - (self.size[0]/2 * self.scale),  
                    center[1] - ((self.size[1]/2 + menu_height/2)*self.scale) 
                    )        
        
    def draw_grid(self, *args):
        print(self.canvas)
        draw_to = self.canvas
        draw_to.clear()

        width = self.width
        height = self.height
        
        print('size is ', width, height)

        color = Color(1, 1, 1, 1)
        draw_to.add(color)

        line = Line(points = (0, 0, width, 0), close = True, width =1)
        draw_to.add(line)


        desired_line_count = 30

        increment_x_by = width/desired_line_count
        increment_y_by = height/desired_line_count

        current_x = 0
        current_y = 0
        

        counter = 0
        while counter <= desired_line_count:
            line = Line(points=(current_x, current_y, current_x, current_y + height),
                        close = True,
                        width = 1)
            draw_to.add(line)
            current_x += increment_x_by
            counter += 1

        counter = 0
        current_x = 0

        while counter <= desired_line_count:
            line = Line(points=(current_x, current_y, current_x + width, current_y)
                        ,close = True,
                        width = 1)
            draw_to.add(line)
            current_y += increment_y_by
            counter += 1