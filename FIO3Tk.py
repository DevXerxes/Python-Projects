# Python Ver:   3.9.7
#
# Author:       Marlon De La Torre
#
# Purpose:      A GUI to make a file transfer program versatile
#               for users to transfer files modified in last 24 hours
#               from a source directory to to detination directory.
#
# Tested OS:    This code was written and tested to work with Windows 10/11.

from tkinter.filedialog import askdirectory
import datetime
from datetime import *
import glob
import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import timedelta
from datetime import datetime


# This is the initiation for the main window for tkinter GUI



def sourceBrowse():
    '''
    Select an Source Folder to look for the text files
    '''
    # The event to help select the source folder
    src = tk.filedialog.askdirectory()
    sourceFolderText.insert(0, src)

def destBrowse():
    '''
    Select a Destinaton Folder to copy the files to
    '''
    dest = tk.filedialog.askdirectory()
    destFolderText.insert(0, dest)


def copyFiles():
    src = sourceFolderText.get()
    des = destFolderText.get()
    sourceFiles = os.listdir(src)
    for i in sourceFiles:
        filePath = os.path.join(src, i)
        timepaste = os.path.getmtime(filePath)
        dateFiletime = datetime.fromtimestamp(timepaste)
        if dateFiletime > (datetime.now()-timedelta(hours = 24)):
            shutil.move(src + "/" + i, des)
            print(i + "Transferred")
       
        


      

m = tk.Tk()

# create the layout for the GUI
    
        
copyTextLabel = tk.Label(m, anchor = "e", text="Copy text files modified since:")
copyTextLabel.grid(column=0, row=1)


# Display the last date and time files were transferred
lastTransferDate = tk.Label(m, anchor="w", text = "24 hours", width=33)
lastTransferDate.grid(column=1, row=1)



# Source folder elements
sourceFolderLabel = tk.Label(m, anchor="e", text="Source Folder:", width=22)
sourceFolderLabel.grid(column=0, row=2)
sourceFolderText = tk.Entry(m, width=100)
sourceFolderText.grid(column=1, row=2)
sourceBrowseButton = tk.Button(m, text="Browse", command=sourceBrowse)
sourceBrowseButton.grid(column=2, row=2, padx=5)


# Destination Folder Elements
destFolderLabel = tk.Label(anchor="e", text="Destination Folder:", width=22)
destFolderLabel.grid(column=0, row=3)
destFolderText = tk.Entry(m, width=100)
destFolderText.grid(column=1, row=3)
destBrowseButton = tk.Button(text="Browse", command=destBrowse)
destBrowseButton.grid(column=2, row=3, columnspan=3, pady=5)

# Copy button element
copyFilesButton = tk.Button(text="Copy Files", command=copyFiles)
copyFilesButton.grid(column=0, row=4, columnspan=3, pady=5)

m.mainloop()


        
