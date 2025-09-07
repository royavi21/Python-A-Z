# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Bangladesh Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, trainNo, fro, to ):
        print(f"Booking ticket in train no {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running and on time")

    def getfare(self, teainNo, fro, to):
        print(f"The fare in train no {self.trainNo} from {fro} to {to} is {randint(111,1500)}")

t = Train(12345)
t.book(12345, "Dhaak", "Khulna")
t.getstatus()
t.getfare(12345, "Dhaka", "Khulna")