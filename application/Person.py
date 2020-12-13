from Address import *

class Person:
    name = "No name"
    address = None
    age = 0
    def __init__(self, name, address_city, address_street, address_number, age):
        self.name = name
        self.address = Address(address_city, address_street, address_number)
        self.age = age
    def print(self):
        print(self.name+" ", end="")
        self.address.print()
        print(" "+str(self.age))
    def get_address(self):
        return self.address.city+" "+self.address.street+" "+str(self.address.number)
    def birthday(self):
        self.age += 1
        print("Happy Birthday "+self.name+"!")
