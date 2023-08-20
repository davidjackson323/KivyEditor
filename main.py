
from kivymd.tools.hotreload.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.core.window import Window
from custom.util import windowSize, mousePosition, scrollsize, drag_and_drop
from custom.util import update_grid
from custom.appview import AppView
from custom.widget_selector import WidgetSelector
from custom.widget_settings import WidgetSettings

from kivy.clock import Clock



from kivy.uix.button import Button
from functools import partial

import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"


print('hello world')
windowSize(5)
Window.bind(on_motion = mousePosition)


class KVEditor(MDApp):
    DEBUG = True
    KV_DIRS = ["custom"]
    #KV_FILES = ["custom/appview.kv"]
    CLASSES = {"AppView": "custom.appview"}
    AUTORELOADER_PATHS = [(os.getcwd(), {"recursive": True}),
                          "custom"]

    def build_app(self, first=False):
        Clock.schedule_once(self.set_page)
        button = Button()
        #Clock.schedule_interval(partial(drag_and_drop, self, button), 0.5)
        return Builder.load_file('screens/home.kv')
    
    def set_page(self, *args):
        #print(self.root.children[0].ids)
        root = self.root.children[0]
        button = Button()
        #drag_and_drop(self, button)
        #root.ids.view_port.grid_lines()


if __name__ == '__main__':
    KVEditor().run()    

