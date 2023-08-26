from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.recycleview import MDRecycleView
#refresh needs diff. approach. See below.
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.responsivelayout import MDResponsiveLayout


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
'''

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