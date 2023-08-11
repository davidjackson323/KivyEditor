from kivy.core.window import Window

def windowSize(monitors = 1):
    if monitors == 1:
        print('setting window size')
        Window.size = (1920/1.1, 1080/1.1)
        Window.top = 20
        Window.left = 3840/2

    if monitors == 2:
        Window.size = (958, 1000)
        Window.top = 31
        Window.left = 6721

    if monitors == 3:
        Window.maximize()
        #window_width = Window.size[1]

        Window.size = (Window.size[0]/2, Window.size[1])
        Window.top = 31
        Window.left = Window.width/2

    if monitors == 4: 
        Window.maximize()
        #Window.left = 0
        #Window.top = -793

def scrollsize(self):
    print(self)

def mousePosition(self, *args):
    #print('moved', self.mouse_pos)
    root_window = self.children[0].children[0]
    root_window.ids.mouse_box.pos = self.mouse_pos
    root_window.ids.mouse_box.text = str(self.mouse_pos)
    print(Window.size, "SIZE")
    print(Window.left, "LEFT")
    #print(Window.top, "TOP")

def drag_and_drop(self, widget = None, *args):
    print(widget)
    print(self.root.mouse_pos)
    #widget.pos = self.mouse_pos
    
