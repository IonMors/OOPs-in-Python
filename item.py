import csv

class Item:
    pay_rate = 0.9
    all = []
    def __init__(self, name: str, price: float, quantity):
        
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than and equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than and equal to zero!"
        
        # Assign to self object
        self.__name = name     # setting private attribute by using 2 underscore
        self.price = price
        self.quantity = quantity
        
        # Actions to execute
        Item.all.append(self)
        
    @property
    #Property decorator = Read-only Attribute
    def name(self):
        return self.__name  # setting private attribute by using 2 underscore
    
    @name.setter    #using setter method to change the value of attribute of the class that is fixed by encapsulation
    def name(self, value):
        print("You are trying to set")
        if len(value) > 10:
            raise Exception("Your name is too long")
        self.__name = value
    
    def calcualte_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        #pay_rate is already there in the class but to access it, it can be done either from class level or from instance level
        #so instead of using Item.pay_rate we will use self.pay_rate to avoid the fix value of pay_rate
        self.price = self.price * self.pay_rate
        
    @classmethod #decorator is used to declare a method in the class as a class method that can be called using ClassName. MethodName()
    def instantiate_from_csv(cls): #here the class reference is passed as a first argument, when we call a class method in this approach
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f) #this method will read the content from csv file as a dictionary
            items = list(reader)
            
        for item in items:
            Item(
                    name = item.get('name'),
                    price = int(item.get('price')),
                    quantity = int(item.get('quantity'))
                )
                        
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):# checking if it is an instance of a float
            #Count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int): # checking if it is an instance of an integer
            return True
        else:
            return False
    
    def __repr__(self): #magic method which returns the object representation in string format
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})" # a generic way to receive class name from the instance

#@property is a built-in decorator for the property() function in Python. 
#It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.
    
   