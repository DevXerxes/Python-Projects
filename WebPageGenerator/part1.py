# Python Version: 3.9.7
#
# Author: Marlon De La Torre
#
# This code constructs a web page generator.
#
# Purpose: Creates a script in Python to generate
# an HTML file in a new web page window.


# import the request module from urllib library
from urllib import request
import webbrowser

# writing the html.py
# here we are creating the html file
f = open('salespitch.html','w')

# here is the html code that will display in new window web page
message = """<html>
<body>
    <h1> Stay tuned for our amazing summer sale!</h1>
</body>
</html>"""

# the method to commit the content
f.write(message)
f.close()

# creating variable for the html file
# to easily access
salesFile = 'C:\WebPageGenerator\salespitch.html'
# the module to open the html file in a new web page
webbrowser.open_new_tab(salesFile)
