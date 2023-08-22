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
        Window.bind(on_mouse_down = self.zoom_wheel)


    def zoom_wheel(self, instance, x, y, button, *args):
        try:
            root = self.get_root_window()
            root = root.children[0].children[0]
            app_view = root.ids.view_port

            if app_view.collide_point(x, y):
                if button == 'scrolldown':
                    self.zoom_in()

                if button == 'scrollup':
                    self.zoom_out()
        except:
            pass


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

    def set_app_size(self, *args, instance=None):
        print(self.ids.app_width.text, self.ids.app_height.text, self.ids.app_scale.text, self.ids.scale_step.text)

        good_to_go = 1

        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port

        original_width = str(app_view.width)
        original_height = str(app_view.height)

        width_input = self.ids.app_width
        height_input = self.ids.app_height

        width = self.ids.app_width.text
        height = self.ids.app_height.text


        try:
            float(width)
        except:
            width_input.text = original_width
            width = original_width
            print('failed to validate, set to original width')

        if float(width) <= 0:
            width_input.text = original_width
            width = original_width

        try:
            float(height)
        except:
            height_input.text = original_height
            height = original_height
            print('failed to validate, set to original height')

        if float(height) <= 0:
            height_input.text = original_height
            height = original_height

        app_view.set_size(width = width, height = height)
        app_view.auto_center()
            

    def set_scale_size(self, *args, instance=None):
        #print(instance.text)
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port
        
        scale_size = instance.text
        try:
            float(scale_size)

        except:
            instance.text = str(int((app_view.scale*100)))
            scale_size = app_view.scale

        if float(scale_size) <= 0:
            scale_size = app_view.scale

        print(app_view.scale)
        scale_size = float(scale_size)
        scale_size = scale_size / 100
        app_view.scale = scale_size

    def set_scale_step(self, *args, instance=None):
        #root = self.get_root_window()
        #app_view = root.children[0].children[0].ids.view_port
        
        scale_step = instance.text

        try: 
            float(scale_step)
        except:
            instance.text = '10'

    def zoom_in(self, *args):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port

        scale_factor = self.ids.scale_step.text
        
        try:
            float(scale_factor)
        except:
            self.ids.scale_step.text = '10'
            scale_factor = 0.1
        
        scale_factor = float(scale_factor) / 100
        app_view.scale += scale_factor
        app_view.auto_center()


    def zoom_out(self, *args):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port

        scale_factor = self.ids.scale_step.text
        
        try:
            float(scale_factor)
        except:
            self.ids.scale_step.text = '10'
            scale_factor = 0.1
        
        scale_factor = float(scale_factor) / 100
        app_view.scale -= scale_factor
        app_view.auto_center()

    def center_app(self, *args):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port
        app_view.auto_center()

    def reset_rotation(self, *args):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port       
        app_view.rotation = 0 

    def rotate_app(self, *args, degrees = 0):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port
        app_view.rotation += degrees

    def rotate_allowed(self, *args, instance = None):
        root = self.get_root_window()
        app_view = root.children[0].children[0].ids.view_port
        rotate_allowed =  app_view.do_rotation
        button = instance
        if rotate_allowed == True:
            button.text = 'Touch Rotation Disabled'
            button.md_bg_color = 0.05, 0.05 ,0.05
            app_view.do_rotation = False
        
        else:
            app_view.do_rotation = True
            button.text = 'Touch Rotation Enabled'
            button.md_bg_color = 0, 0, 1, 1

    

