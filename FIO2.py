import shutil
import os
import datetime
import glob

def GetFileList(path, type):
    '''
    Return a list of file name matching the given path and file type
    '''

    return glob.glob(path + "*" + type)

# set where the source of the new/edited daily files are at
source = '../Users/vidin/OneDrive/Desktop/DailyInput/'

# set the destination path to HomeOffice folder
destination = '../Users/vidin/OneDrive/Desktop/HomeOffice/'
# use the os.listdir() function for listing all files in this source folder
fileType = ".txt"


# Below creates a list of text filenames in Source folder
fileList = GetFileList(source, fileType)

# for loop to acquire the file modified in last 24 hours
for file in fileList:
    # Get last modified date and today's date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()

    filePathList = file.split("\\") # Create a list from the filepath
    filename = filePathList[-1] # The last element is the a filename

    # If modified within last 24 hours, then file is copied to destination folder
    modifyDateLimit = modifyDate + datetime.timedelta(days=1)

    # If the file was edited less than 24 hours ago then copy it
    if modifyDateLimit > todaysDate:
        shutil.copy2(file, destination + filename)



