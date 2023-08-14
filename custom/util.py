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
        Window.size_hint_x: None
        Window.size = (0.5, 100)
        Window.left = Window.width
        #Window.height = Window.height/2
        #Window.top = -793

    if monitors == 5:
        #Window.maximize()
        #print(window.size)
        Window.size = (1883, 1016)
        Window.top = 31
        Window.left = 2010


def scrollsize(self):
    print(self)


def mousePosition(self, *args):
    #print('moved', self.mouse_pos)
    root_window = self.children[0].children[0]
    root_window.ids.mouse_box.pos = self.mouse_pos
    root_window.ids.mouse_box.text = str(self.mouse_pos)

    #getting the view_port location, size and position, to check if we are in bounds
    view_port = root_window.ids.view_port

    #for the bounds checking we need to make sure that we are checking
    #if the mouse location is with in the designated space for clicking
    #or if the view is zoomed in, then check if if the mouse is in the 
    #the view_port. 
    #Currently we have the second of the later.
    #We can use the scale to do set up the if statement. If scale bigger than 1
    #default to inside of designated space. 

    print("COLLISION DETECTED", view_port.collide_point(self.mouse_pos[0], self.mouse_pos[1]))



def drag_and_drop(self, widget = None, *args):
    print(widget)
    print(self.root.mouse_pos)
    #widget.pos = self.mouse_pos
    
