class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically call
        self.name = name
        self.salary = salary
        self.language = language
        print("Creating an object")
    def getinfo(self):
        print(f"the language is {self.language} and Salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

Shahzad = Employee("Shezi", 1500000, "Js")
# Shahzad.language = "Javascript"
print(Shahzad.language, Shahzad.salary, Shahzad.name)
Shahzad.getinfo()
Shahzad.greet()
# Aman = Employee()
# Aman.name = "Aman"
# print(Aman.name, Shahzad.language, Shahzad.salary)