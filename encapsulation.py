

class VPN:
    def __init__(self):
        # setting the obj up with a variable
        self.__privatePage = 'Home Page'
        self._privatePage = 'Home Page'

    def getPrivate(self):
        print(self.__privatePage)

    def setPrivate(self, private):
        # Here i am making the object private with double underscore
        self.__privatePage = private

# Setting the object to be protected with the Protected() method
obj = VPN()
obj.getPrivate() 
#Here i am connecting the Protected() method with the object variable
# to get the object protected and private
obj.setPrivate('Content Page')
obj.getPrivate()
