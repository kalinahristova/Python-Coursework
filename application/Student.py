from Person import *

class Student(Person):
    program = ""
    year = 0
    fee = 0.00
    def __init__(self, name, address_city, address_street, address_number, age, program, year, fee):
        self.program = program
        self.year = year
        self.fee = fee
        self.name = name
        self.age = age
        self.address = Address(address_city, address_street, address_number)
    def print(self):
        print(self.name+"; Age: "+str(self.age))
        print("Address: "+self.get_address())
        print("Program: "+self.program+"; Year: "+str(self.year)+"; Fee: ", end="")
        print(f'{self.fee:.2f}')
    def graduate(self):
        if self.year == 4:
            print(self.name+" can gradueted!")
        else:
            print(self.name+" can onli graduated if year = 4!")
    def finish_year(self):
        print(self.name+" is finised year "+str(self.year)+"!")
        self.year += 1
        self.fee = 1.1 * self.fee
