from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"



class AppView(ScatterLayout):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        #print(self.canvas)
        print('STARTING X IS', self.x)
        self.starting_x = self.x
        Clock.schedule_once(self.grid_lines, 1)
        #self.grid_lines(canvas=self.canvas)

    def allow_rotation(self, instance, *args):
        if self.do_rotation == False:
            self.do_rotation = True
            instance.md_bg_color = (0, 0, 0, 1)
            instance.text = "Touch Rotation Enabled"

        else: 
            self.do_rotation = False
            instance.md_bg_color = (1, 0, 0, 1)
            instance.text = "Touch Rotation Disabled"

    def grid_lines(self, canvas=None, *args):
        
        draw_to = self.canvas

        height = self.height
        width = self.width
        scale = self.scale
        
        relative_size = self.size
        window_size = self.get_root_window().size

        actual_size_x = relative_size[0] * window_size[0] * scale
        actual_size_y = relative_size[1] * window_size[1] * scale
        # print(self.size, self.get_root_window().size)
        # print("actual size is", actual_size_x, actual_size_y)




        desired_line_count = 15

        increment_x_by = actual_size_x/desired_line_count
        increment_y_by = actual_size_y/desired_line_count

        current_x = 0
        current_y = 0

        color = Color(1, 1, 1, 1)
        draw_to.add(color)
    
        counter = 0

        #Draw lines across x axis
        while counter <= desired_line_count:
            line = Line(points=(current_x, current_y, current_x, current_y + actual_size_y),
                        close = True,
                        width = 1)
            draw_to.add(line)
            current_x += increment_x_by
            counter += 1

        counter = 0
        current_x = 0

        while counter <= desired_line_count:
            line = Line(points=(current_x, current_y, current_x + actual_size_x, current_y)
                        ,close = True,
                        width = 1)
            draw_to.add(line)
            current_y += increment_y_by
            counter += 1


    def reset_rotation(self, *args):
        self.rotation = 0

    def reset_zoom(self, *args):
        self.scale = 1
        self.rotation = 0
        self.x = (self.starting_x)  
        self.y = 0



    def zoom_out(self, *args):
        if self.scale > 0.4:
            self.scale -= 0.1


    def zoom_out_backup(self, *args):
        print(self.size, 'Appview Size')
        print(self.scale, 'Appview scale')
        print(self.parent.id, self.parent.size, "AppView Container Size")
        print(self.parent.x, 'App Container Position')

        if self.scale > 0.4:
            self.scale -= 0.1
            adjust_x = ((1 - self.scale) * self.parent.width)/2.5
            self.x = adjust_x + (self.parent.x * 0.5)
            print("adjust x is", adjust_x, "and self x", self.x, "and parent is ", self.parent.x)


            adjust_y = ((1 - self.scale) * self.parent.height)/4
            self.y = adjust_y + (self.parent.y * 0.5)
            print("adjust y is", adjust_y, "and self y", self.y, "and parent is ", self.parent.y)


    def zoom_in(self, *args):

        if self.scale < 1.4:
            self.scale += 0.1



    def zoom_in_backup(self, *args):

        if self.scale < 1.4:
            self.scale += 0.1
            adjust_x = ((1 - self.scale) * self.parent.width)/2.5
            self.x = adjust_x + (self.parent.x * 0.5)
            print("adjust x is", adjust_x, "and self x", self.x, "and parent is ", self.parent.x)


            adjust_y = ((1 - self.scale) * self.parent.height)/4
            self.y = adjust_y + (self.parent.y * 0.5)
            print("adjust y is", adjust_y, "and self y", self.y, "and parent is ", self.parent.y)

        
        
