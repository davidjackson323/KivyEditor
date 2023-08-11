from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import Rectangle, Line, Color
from kivy.core.window import Window 


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
        #self.grid_lines()
        #print('hello')

    def grid_lines(self, *args):
        draw_to = self.canvas

        height = self.height
        width = self.width


        
        
        #position = self.parent.pos
        #x_pos = position[0]
        #print(self.parent.size)
        relative_x = self.parent.size_hint_x
        window_width = Window.width
        window_height = Window.height
        width = (relative_x * window_width)
        self.width = width
        #relative_y = self.parent.size_hint_y
        #y = self.pos[0]
        #height = 10000
        print(height, width, "is height and width")
        
        #y_pos = 0

        

        # x_pos = (window_width * relative_x) - width

        line_x_count = 20
        increment_width_by = width/line_x_count
        x_pos = 95
        # line_y_count = 10
        # increment_height_by = height/line_y_count

        current_x = x_pos
        color = Color(1, 1, 1, 1)
        draw_to.add(color)

        while current_x <= x_pos + width:
            line = Line(points=(current_x, 0, current_x, Window.height),close = True)
            draw_to.add(line)
            current_x = current_x + increment_width_by

        
    
    #Builder.load_file('custom/appview.kv')
