#
# Author: Marlon De La Torre
#
# This code constructs a GUI(Graphical User Interface)
# using Tkinter module.
#
# Purpose: Creates a GUI in Python, using Tkinter to generate
# an HTML file of the users choice in a new web page window.

from tkinter import *
import webbrowser
import tkinter as tk
from urllib import request

def urPage():
    
    # writing the html.py
    # here we are creating the html file
    f = open('indexWB.html','w')
    # here is where we make our inputted body text as a source to then
    #display it into the newly generated web page
    text = source.get()
    # here is the html code that will display in new window web page
    message = """<html>
    <head></head>
    <body>
        <h1>%s</h1>
    </body>
    </html>""" % text
    # the method to commit the content
    f.write(message)
    f.close()
    # creating variable for the html file
    # to easily access
    NewPage = 'indexWB.html'
    # the module to open the html file in a new web page
    webbrowser.open_new_tab(NewPage)

        
# here we make the GUI into shorter variable
wbGUI = Tk()
# here we are assigning the source of the inputted body text
# as a string value
source = StringVar()

# setting the size of the GUI and the title
wbGUI.geometry('450x450+500+300')
wbGUI.title('Web Page Generator')

wblabel = Label(wbGUI, text='Type Your Body Text Below').pack()

wbbutton = Button(wbGUI, text='Open Your New Web Page', command=urPage).pack()

wbentry= Entry(wbGUI, textvariable=source).pack()

wbbutton= Button(wbGUI, text='Close Program', command= lambda: ask_quit(self))






def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit the application?"):
        # This closes app
        self.master.destroy()
        os.exit(0)



if __name__ == "__main__":
    root = tk.Tk()
    App = urPage(root)
    root.mainloop()
