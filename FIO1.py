import shutil
import os

# set where the source of the files are
source = '../Users/vidin/OneDrive/Desktop/FolderA/'

# set the destination path to Folder B
destination = '../Users/vidin/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
    # we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
    while i in files:
        ('New', 'modified in last 24 hours')
