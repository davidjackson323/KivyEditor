# KivyEditor
This is a project for a Graphical User Interface editor that can be used to develop custom GUI's with Python, Kivy and KivyMD, and is a work in progress currently.
My goal for this project is to allow people to design an app using a point and click style interface, and then to be able to export the application directly to a
python file, the kv file, or even an .EXE to allow for demonstration or development purposes. Once a user has their front end interface developed, they can connect their
back end code to the front end to have a fully functioning application.

Ideally, a user will be able to select widgets from the widget options on the left hand pane of the program. Once the desired widget is clicked, it will be added to the 
app view, seen at the center of the program in the blue box. The app has been designed so that it is scalable, rotatable, resizeble, and recolorable as needed. 
Once a widget is added to the the app view box, all the configurable settings will auto populate on the widget settings pane, seen on the right hand side. 
With these options now available, the user will be able to change size, location, color, text, rotation, and any other settings relevant to that widget. 

While not complete, I decided to make this public in the hopes that it might benefit the open source community, Kivy and the KivyMD libraries that I love working with. 

Thanks for checking out the application. Development will be happening steadily as I balance coding with my educational pursuits, so stay tuned for progress. 


![Screenshot from 2023-08-25 10-06-41](https://github.com/davidjackson323/KivyEditor/assets/19483270/0da6c880-58a0-4d74-a5bf-0ee5e22f5a71)

https://youtu.be/TBQq0OQxd-8




https://github.com/davidjackson323/KivyEditor/assets/19483270/bf9cae57-b9bb-4819-be8b-ff7c0e820398


TODO:  
Begin integrating each individual widget seen in the widget options pane.  
Implement the logic for tracking added widgets and layouts.  
Implement the layout children logic, that identifies what widgets are in the current layouts.  
Implement the boundary checking to identify what widget is being selected by the mouse.  
Implement a highlight feature based upon the boundary checking to highlight the currently hovered over widget/layout.  
Implement the export to python feature.  
Implement the export Kivy file feature.  
Implement the export to EXE feature using pyinstaller.   


