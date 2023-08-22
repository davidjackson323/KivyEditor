
from kivymd.tools.hotreload.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from custom.util import mousePosition, scrollsize, drag_and_drop
from custom.util import update_grid, auto_size
#from custom.appview import AppView
from custom.app_view import AppView
from custom.widget_selector import WidgetSelector
from custom.widget_settings import WidgetSettings
from custom.appview_controls import AppViewControls
from kivy.clock import Clock
from kivy.uix.button import Button
from functools import partial


import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


print('hello world')
#windowSize(5)
#auto_size()

Window.minimum_width = 1500
Window.minimum_height = 500

Window.maximize()
print("WINDOW WIDTH IS", Window.width)
if Window.width > 799:
    Window.restore()
    Window.size = (1883, 1016)
    Window.left = 2010

#Window.bind(on_motion = mousePosition)


class KVEditor(MDApp):
    DEBUG = True
    KV_DIRS = ["custom"]
    #KV_FILES = ["custom/appview.kv"]
    CLASSES = {"AppView": "custom.app_view"}
    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True}),
                          "custom"]

    def build_app(self, first=False):
        Clock.schedule_once(self.set_page, 3)
        #Clock.schedule_once(self.add_buttons, 5)
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
        #root.ids.view_port.draw_grid()

        button = Button()
        button.pos_hint = {'center_x':0.5, 'center_y':0.5}
        button.size_hint = 1, 1
        #button.bind(on_release = print('hello'))
        #root.ids.view_port.add_widget(button)

    def add_buttons(self, *args):
        root = self.root.children[0]
        button = Button()
        button.pos_hint = {'center_x':0.5, 'center_y':0.5}
        button.size_hint = 1, 1
        #button.bind(on_release = print('hello'))

        root.ids.view_port.add_widget(button)


if __name__ == '__main__':
    KVEditor().run()    

