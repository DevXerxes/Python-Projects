#importing the sqlite module to be able to use sql code
import sqlite3

#establishing the connection to the database
#using the connect() module
conct = sqlite3.connect('Animals.db')

#.cursor() method operates the database when
#commands are given
with conct:
    cur = conct.cursor()
    #.execute() allows to create a database in Python
    cur.execute("CREATE TABLE IF NOT EXISTS Animals( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_aName TEXT, \
        col_files TEXT \
        )")
    #Here commit() method establishes the above values into the database
    conct.commit()
#close() closes the connection to prevent memory leaks
conct.close()

conct = sqlite3.connect('Animals.db')

#Here using execute() to input values into database
with conct:
    cur = conct.cursor()
    cur.execute("INSERT INTO Animals(col_aName, col_files) VALUES (?,?)", \
                ('Wolf', 'Habitat.txt'))
    cur.execute("INSERT INTO Animals(col_aName, col_files) VALUES (?,?)", \
                ('Hawk', 'Nutrition.txt'))
    conct.commit()
conct.close()


conct = sqlite3.connect('Animals.db')

#tuple of file names
filesList = ('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# looping through each object in tuple to find file ending in .txt.
for x in filesList:
    if x.endswith('.txt'):
        with conct:
            cur = conct.cursor()
            #value for each row will be one name out of tuple therefore (x,)
            # will denote a one lement tuple for each name ending in .txt.
            cur.execute("INSERT INTO Animals(col_files) VALUES(?)", (x,))
            print(x)


conct.close()

