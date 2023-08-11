from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 
from kivy.clock import Clock
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


appview = """
<AppView>
    Scatter:
        md_bg_color: 1, 1, 1, 1
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        size_hint_x: self.parent.size_hint_x: 0.5
        size_hint_y: self.parent.size_hint_y: 0.5



"""

class AppView(ScatterLayout):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        #print(self.canvas)
        Clock.schedule_once(self.grid_lines)
        #self.grid_lines(canvas=self.canvas)

    def allow_rotation(self, instance, *args):
        if self.do_rotation == False:
            
            self.do_rotation = True
            instance.md_bg_color = (0, 0, 0, 1)
            instance.text = "Touch Rotation Enabled"

        else: 
            self.rotation = False
            instance.md_bg_color = (1, 0, 0, 1)
            instance.text = "Touch Rotation Enabled"

    def grid_lines(self, canvas=None, *args):
        #print('DRAWING GRID LINES')
        #print(self.graphics, "CANVAS LOCATION")
        draw_to = self.canvas
        #print(draw_to)
        
        height = self.height
        width = self.width + 100
        start_x = self.x + 100
        start_y = self.x

        # with self.canvas as canvas:
        #     print(self.pos, self.size)

        #     color = Color(1, 1, 1, 1)
        #     draw_to.add(color)
        
        #     line = Line(points=(start_x, start_y, start_x, start_y + 1000),close = True)
        #     draw_to.add(line)

    def reset_rotation(self, *args):
        self.rotation = 0

    def reset_zoom(self, *args):
        self.scale = 1
        self.rotation = 0
        self.x = (self.parent.pos[0]*0.5)  
        self.y = 0
        self.size_hint = [1, 1]


    def zoom_out(self, *args):
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
            adjust_x = ((1 - self.scale) * self.parent.width)/2.5
            self.x = adjust_x + (self.parent.x * 0.5)
            print("adjust x is", adjust_x, "and self x", self.x, "and parent is ", self.parent.x)


            adjust_y = ((1 - self.scale) * self.parent.height)/4
            self.y = adjust_y + (self.parent.y * 0.5)
            print("adjust y is", adjust_y, "and self y", self.y, "and parent is ", self.parent.y)

        
        
