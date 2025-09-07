# 6. Can you change the self-parameter inside a class to something else (say "ovik"). Try changing self to “slf” or "ovik" and see the effects. 

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        # self is changed to slf
        # লিখার সময় self দিয়ে লিখতে হবে, কিন্তু অন্যকিছু দিয়ে লিখলেও কাজ করবে
        

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