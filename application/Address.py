class Address:
    city = "No City"
    streeet = "No Street"
    number = 0
    def __init__(self, city, street, number):
        self.city = city
        self.street = street
        self.number = number
    def print(self):
        print("["+self.city+" "+self.street+" "+str(self.number)+"]", end="")
