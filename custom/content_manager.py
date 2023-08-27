from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.recycleview import MDRecycleView
#refresh needs diff. approach. See below.
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivy.clock import Clock


'''
The following imports have been commented out as they 
may require different methods of implementation
I'll add the documentation to any such imports. 
'''
#from kivymd.uix.refreshlayout import MDRefreshLayout
#https://kivymd.readthedocs.io/en/1.1.1/components/refreshlayout/

'''
The approach I would like to take, involves keeping a list of all
the layouts and widgets that are added to the program. 

I want this list to have a heirachy of layouts. Anything added to the 
layout will be added as a sublist to that layout. 

This way I can recursively extract the code and structure of the program,
and assemble it using a custom built parser. 

I need to create a master list that is an attribute to something. 
I'm not sure if I can create that attribute in the build_app section
as it doesn't immediately make sense for me.

Instead of keeping track of all the possible widget options,
is there a way to recursively check the available functions, and 
attributes? This might be the most effective way to do so, for a 
lazy/effecient programmer. 
'''

class ContentManager():
    def __init__(self) -> None:
        self.widget_list = [['layouts go here', 'widgets', 'go', 'here', ['nesting', 'testing']], 
                            ['New layout', 'more', 'widgets']]
        self.app_view = None
        self.main = MDApp.get_running_app()
        Clock.schedule_once(self.get_appview, 0.5)

    def get_appview(self, *args):
        self.app_view = self.main.root_window.children[0].children[0].ids.view_port

    def add_to(self, widget_to_add = None):
        test_layout = MDFloatLayout()
        test_layout.pos_hint = {'center_x':0.5, 'center_y':0.5}
        test_layout.size_hint = 0.95, 1
        test_layout.md_bg_color = [1, 1, 1, 1]
        self.app_view.children[0].add_widget(test_layout)
        print(self.app_view.children[0].children)

    def remove(widget_to_remove = None):
        pass
        
    def export_kv():
        pass

    def export_py():
        pass

    def export_exe():
        pass

    def clipboard():
        pass
    

def add_mdfloatlayout(self, *args):
    pass

def add_mdrelativelayout(self, *args):
    pass

def add_mdboxlayout(self, *args):
    pass

def add_mdgridlayout(self, *args):
    pass

def add_mdscrollviewlayout(self, *args):
    pass

def add_mdrecycleviewlayout(self, *args):
    pass

def add_mdrelativelayout(self, *args):
    pass

def add_mdresponsivelayout(self, *args):
    pass