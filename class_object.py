class employee:
    name = "Rakesh"   # name, language, city and salary are attributes of the class employee
    language = "Python"
    city = "Delhi"
    salary = 500000

#print(employee.name, employee.salary) this is also valid but we can also create an object of the class and then access the attributes using that object.

person = employee()   # person is object
print(person.name, person.salary, person.language.upper()) 

# when we put multiple employees data

class multi_employee:
    language = "HTML"
    city = "Surat"
    salary = 5000000

harry = multi_employee()
name = "harry"
print(name, ":-", harry.language, harry.city, harry.salary)

rohan = multi_employee()
name = "rohan"
print(name, ":-", rohan.language, rohan.city, rohan.salary)

shubham = multi_employee()
name = "shubham"
print(name, ":-", shubham.language, shubham.city, shubham.salary)


# instance vs class

# Python check instance variable first and then class variable. If thier is not instance variable then it prints class variable
class Employee:
    language = "Python"  # This is class variable
    city = "Surat"

harry = Employee()
harry.language = "HTML" # This is instance variable
print(harry.language, harry.city)  # Instance varialbe prints not class variable


# oop with function (self parameter)

class company:
    name1 = "Google"
    name2 = "Amazon"
    name3 = "Microsoft"

    def getInfo(self):
        print(f"The learning language is {self.language}. The company name is {self.name1}")
        print("Company name is:", self.name1)
        print("Company name is:", self.name2)
        print("Company name is:", self.name3)

executive = company()
executive.language = "Java"
executive.getInfo()
print()

class company:
    name1 = "Google"
    salary1 = 50000
    name2 = "Amazon"
    salary2 = 45000
    name3 = "Microsoft"
    salary3 = 56000

    def data(self):
        print(f"The learning language is {self.language}. The company name is {self.name1}. The salary is {self.salary1}")
        print(f"The learning language is {self.language}. The company name is {self.name2}. The salary is {self.salary2}")
        print(f"The learning language is {self.language}. The company name is {self.name3}. The salary is {self.salary3}")

    # def greet(self):
    #   print("Good Morning")
    @staticmethod     # They didn't needs object in def greet function
    def greet():
        print("Good Morning")
    

executive = company()
executive.language = "Java"
executive.greet()
executive.data()


# __int__ constructor

class company:
    language = "Python"
    city = "Delhi"
    salary = 500000

    def __init__(self):     # Run automatically without call the function when object created
        print("Program started")

employees = company()
name = "Rakesh"
print(name, ":-", employees.language, employees.salary, employees.city)
employees1 = company()

class company2:
    language = "Python"
    city = "Surat"
    salary = 900000

    def __init__(self, name, salary, city):
        self.name= name
        self.salary = salary
        self.city = city
        print("started")
    
jal = company2("Jal", 900000, "Delhi")
jal.name = "jal"
print(jal.name, jal.language, jal.salary, jal.city)
