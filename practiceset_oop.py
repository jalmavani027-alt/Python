# # Q 1 :- Create a class “Programmer” for storing information of few programmers working at
# # Microsoft.

# class programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin

# p1 = programmer("Jayesh", 50000, 110011)
# p2 = programmer("Hitesh", 60000, 110022)
# p3 = programmer("Suresh", 70000, 110033)
# print("Name:-", p1.name, "Salary:-", p1.salary, "Pin:-", p1.pin, "Company Name:-", p1.company)
# print("Name:-", p2.name, "Salary:-", p2.salary, "Pin:-", p2.pin, "Company Name:-", p2.company)
# print("Name:-", p3.name, "Salary:-", p3.salary, "Pin:-", p3.pin, "Company Name:-", p3.company)


# # Q 2 :- Write a class “Calculator” capable of finding square, cube and square root of a number.

# class calculator:
#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         return self.number ** 2

#     def cube(self):
#         return self.number ** 3

#     def square_root(self):
#         return self.number ** 0.5

# a = int(input("Enter a number: "))
# calc = calculator(a)

# print("Square of", calc.number, "is", calc.square())
# print("Cube of", calc.number, "is", calc.cube())
# print("Square root of", calc.number, "is", calc.square_root())

# # Another way to call the function

# calc.square()
# calc.cube()
# calc.square_root()
# print("This is square of input number:-", calc.square())
# print("This is cube of input number:-", calc.cube())
# print("This is square root of input number:-", calc.square_root())


# Q 3 :- Create a class with a class attribute a; create an object from it and set ‘a’ directly using
# ‘object.a = 0’. Does this change the class attribute?

# class demo:
#     a = 150

# o = demo()
# print(o.a)

# o.a = 0
# print(o.a)  # This will print 0, but it does not change the class attribute 'a'
# print(demo.a)  # This will still print 150, showing that the class attribute remains unchanged

# # That's why class attribute never change they remains same but due to instance attribute the value is changed for that particular object


# # Q 4 :- Add a static method in problem 2, to greet the user with hello

# class calculator:
#     def __init__(self, number):
#         self.number = number

#     def square(self):
#         return self.number ** 2

#     def cube(self):
#         return self.number ** 3

#     def square_root(self):
#         return self.number ** 0.5

#     @staticmethod
#     def greet():
#         print("Hello! Welcome to the my Calculator program.")

# a = int(input("Enter a number: "))
# calc = calculator(a)

# calc.greet()
# print("Square of", calc.number, "is", calc.square())
# print("Cube of", calc.number, "is", calc.cube())
# print("Square root of", calc.number, "is", calc.square_root())


# Q 5 :- Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.

import random

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def booking(self, fro, to):
        print(f"Booking a ticket for {self.trainNo} from {fro} to {to}")
              
    def get_status(self):
        print(f"Status of train {self.trainNo} is running on time") 
        
    def get_fare_info(self, fro, to):
        print(f"Fare information for {self.trainNo} from {fro} to {to} is {random.randint(100, 1000)}")

t = train(1234)
t.booking("Surat", "Delhi")
t.get_status()
t.get_fare_info("Surat", "Delhi")


# Q 6 :- Can you change the self-parameter inside a class to something else (say “harry”)? Try
# changing self to “slf” or “harry” and see the effects.

# Nothing change if we change the self parameter to something else, it will still work as long as we use that new name consistently within the class methods. The self parameter is just a convention and can be replaced with any valid identifier.

# But it is not good practice to change the self parameter name, as it can lead to confusion for other developers reading the code. It is recommended to stick with the convention of using 'self' for clarity and maintainability.

