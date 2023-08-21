
from kivymd.tools.hotreload.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from custom.util import windowSize, mousePosition, scrollsize, drag_and_drop
from custom.util import update_grid
#from custom.appview import AppView
from custom.app_view import AppView
from custom.widget_selector import WidgetSelector
from custom.widget_settings import WidgetSettings
from kivy.clock import Clock
from kivy.uix.button import Button
from functools import partial


import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


print('hello world')
windowSize(5)
#Window.bind(on_motion = mousePosition)


class KVEditor(MDApp):
    DEBUG = True
    KV_DIRS = ["custom"]
    #KV_FILES = ["custom/appview.kv"]
    CLASSES = {"AppView": "custom.app_view"}
    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True}),
                          "custom"]

    def build_app(self, first=False):
        Clock.schedule_once(self.set_page, 2)
       
        button = Button()
        #Clock.schedule_interval(partial(drag_and_drop, self, button), 0.5)
        return Builder.load_file('screens/home.kv')
    
    def set_page(self, *args):
        #pass
        #print(self.root.children[0].ids)
        root = self.root.children[0]
        root.ids.view_port.set_size(width = 1920, height = 1080)
        
        root.ids.view_port.auto_center()
        root.ids.view_port.scale = 0.65
        root.ids.view_port.draw_grid()
        #root.ids.view_port.set_size()
        #center_appview = root.ids.test_resize.size[0]/2
        #widget = root.ids.test_resize
        #root.ids.test_resize.pos = Window.center[0] - (widget.size[0]/2), Window.center[1] - (widget.size[1]/2)


        '''
        The Scatter layout does not work as expected.
        Really sucks butt, and I'm not willing to waste early
        development time figuring out the kinks.

        Will create a Relative Layout and figure shit out from there.
        
        #maybe not. reworking with it, it appears the grid draw feature 
        is whats causing the resizing problems. Will need to look into that more
        '''



    


if __name__ == '__main__':
    KVEditor().run()    

