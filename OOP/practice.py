# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p = Programmer("Shahzad", 1200000, 2300)

# print(p.name, p.company, p.pin, p.salary)


# class Calculator:
#     def __init__(self, n):
#         self.n = n
    
#     def square(self):
#         print(f"The square is {self.n * self.n}")
    
#     def cube(self):
#         print(f"The cube is {self.n * self.n * self.n}")
    
#     def squareroot(self):
#         print(f"The squareroot is {self.n ** 1/2}")
    
#     @staticmethod
#     def Cool():
#         print("Hello Cool")

# a = Calculator(4)
# a.Cool()
# a.square()
# a.cube()
# a.squareroot()

# class Demo:
#     a = 4

# o = Demo()
# print(o.a) # print class attribute because instance attribute is not present  
# o.a = 0 # instance attribute is set
# print(o.a)  # print instance attribute because instance attribute is present
# print(Demo.a) # print the class attribute

# from random import randint
# class Train:

#     def book(self, trainNo, fro, to):
#         print(f"Ticket is booked in train no: {trainNo} from {fro} to {to}")

#     def getStatus(self, trainNo):
#         print(f"Train no: {trainNo} is running on time")

#     def getFare(self, trainNo, fro, to):
#         print(f"Ticket fare in train no: {trainNo} from {fro} to {to} is {randint(22, 55)}")


# t = Train()
# t.book(23, "Karachi", "Lahore")
# t.getFare(23, "Karachi", "Lahore")