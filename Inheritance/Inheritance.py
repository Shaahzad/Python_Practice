# class TwoDVector:
#     a = 1

#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The vector is {self.i} i + {self.j} j")

# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


# a = TwoDVector(1, 2)
# a.show()
# b = ThreeDVector(1,2,3)
# b.show()


# class Animal:
#     pass

# class Pets(Animal):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")

# d = Dog()
# d.bark()


# class Employee:
#     salary = 234
#     increment = 20
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))
    
#     @salaryAfterIncrement.setter
#     def salaryafterincrement(self, salary):
#         self.increment = ((salary/self.salary) -1)*100

    
# e = Employee()
# # print(e.salaryAfterIncrement)
# e.salaryafterincrement = 280.8
# print(e.increment)