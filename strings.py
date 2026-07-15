# Types of Strings
a = "jal"
b = 'jalm'
c = '''coding is
    best mental 
    exercise in the
    world'''   #This string use for paragraph writings



print(a)
print()
print() # to make empty spaces 

print(b)
print()
print()

print(c)


# practice set

a = input("Enter your name: ")
print("Hello " + a + " \nGood Morning")

b = input("Enter your name: ")

print(f" Good Evening \n {b.capitalize()}")



# 2 

a = ''' dear |name| 
  you are selected for this job role
  |date|'''

print(a.replace("|name|", "Jal Mavani").replace("|date|", "12/4/2023"))



#3 

a = "jal"
print(a[0:2]) 

b = "mavani  "
print(len(b))

a = "i am very  good boy in the world"
print(a.find("  "))



# 4

a = "i am very  good boy in the world"
print(a.replace("  ", " "))


# 5

letter = "dear man, \nthis course is very good. \nThanks a lot!"
print(letter)