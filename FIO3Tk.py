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
import glob
import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox


# This is the initiation for the main window for tkinter GUI
class mainWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("File Transfer Process")
        self.parent.geometry("")
        arg = self.parent
        self.initialize()

    # the function to create the layout for the GUI
    def initialize(self):
        

        self.grid()

        self.copyTextLabel = tk.Label(self, anchor = "e", text="Copy text files modified since:")
        self.copyTextLabel.grid(column=0, row=1)


        # Display the last date and time files were transferred
        self.lastTransferDate = tk.Label(self, anchor="w", text = "24 hours", width=33)
        self.lastTransferDate.grid(column=1, row=1)
        


        # Source folder elements
        self.sourceFolderLabel = tk.Label(self, anchor="e", text="Source Folder:", width=22)
        self.sourceFolderLabel.grid(column=0, row=2)
        self.sourceFolderText = tk.Text(self, state="disabled", width=30, height=1)
        self.sourceFolderText.grid(column=1, row=2)
        self.sourceBrowseButton = tk.Button(self, text="Browse", command=self.sourceBrowse)
        self.sourceBrowseButton.grid(column=2, row=2, padx=5)


        # Destination Folder Elements
        self.destFolderLabel = tk.Label(self, anchor="e", text="Destination Folder:", width=22)
        self.destFolderLabel.grid(column=0, row=3)
        self.destFolderText = tk.Text(self, state="disabled", width=30, height=1)
        self.destFolderText.grid(column=1, row=3)
        self.destBrowseButton = tk.Button(self, text="Browse", command=self.destBrowse)
        self.destBrowseButton.grid(column=2, row=3, columnspan=3, pady=5)

        # Copy button element
        self.copyFilesButton = tk.Button(self, text="Copy Files", command=self.copyFiles)
        self.copyFilesButton.grid(column=0, row=4, columnspan=3, pady=5)


    def sourceBrowse(self):
        '''
        Select an Source Folder to look for the text files
        '''

        # The event to help select the source folder
        dlg = tk.filedialog.askdirectory(parent=self, initialdir="/", title="Choose the Source Folder:")
        print(dlg)
        if len(dlg) > 0:
            self.destFolderText.config(state="normal")
            self.destFolderText.delete('1.0', 'end')
            self.destFolderText.insert('1.0', dlg)
            self.destFolderText.config(state="disabled")


    def destBrowse(self):
        '''
        Select a Destinaton Folder to copy the files to
        '''
        
        dlg2 = tk.filedialog.askdirectory(parent=self, initialdir="/", title="Choose Destinaton Folder:")
        print(dlg2)
        if len(dlg2) > 0:
            self.destFolderText.config(state="normal")
            self.destFolderText.delete('1.0', 'end')
            self.destFolderText.insert('1.0', dlg2)
            self.destFolderText.config(state="disabled")


    def copyFiles(self):
        # Perform the copy function on files

        # Find the source and destination paths (new lines will need to be replaced)
        sourcePath = self.sourceFolderText.get('1.0', 'end').replace('\n','') + "\\"
        destPath = self.destFolderText.get('1.0', 'end').replace('\n','') + "\\"

        fileType = ".txt"


        # Create list of text filenames in source folder
        fileList = glob.glob(sourcePath + "*" + fileType)



        for file in fileList:
            # get last modified date and today's date
            modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))

            filePathList = file.split("\\") # Create a list from the filepath
            filename = filePathList[-1] # the last element is the filename


            if modifyDate > dtLastDateTime:
                shutil.copy2(file, destPath + filename)


        # Insert new row into the database
        todaysDate = datetime.datetime.today().strftime("%m-%d-%Y %H:%M:%S")
        


        # Update GUI with new date and time
        self.lastTransferDate.config(text=todaysDate)


if __name__=="__main__":
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()


        
