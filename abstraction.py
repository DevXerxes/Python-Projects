# need to omport the abstraction method from the ABC module
from abc import ABC, abstractmethod
class store(ABC):
    def receipt(self, amount):
        print("Amount of item: ",amount)
# this function is saying to pass in an argument, but it wont say how or what
# kind of data it will be.
# Here i am using the abstractmethod
    @abstractmethod
    # here is the regular method
    def urpayment(self, amount):
        pass


#Here is the child class the defines the implementation of the
    #the parent abstract method
class DeclinedPayment(store):
# here we've defined how to implement the urpayment function from its parent receipt class.
    def urpayment(self, amount):
        print("Your payment type declined the amount of {}, please enter another method of payment.".format(amount))


# here is the values inputted and being implemented in the abstraction method with the functions of the classes above
obj = DeclinedPayment()
obj.receipt("$1,200")
obj.urpayment("$1,200")
