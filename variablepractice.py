# Today, we understand variables and some functions

a = "start"
print(a)

b = 5
c= 10
print(b+c)

# let's understand the type function

a = 50
b = type(a)
print(b)   # output:- "integer"

l = 50.67
m = type(l)
print(m)    # output:- "float"

l = 50.67
print(type(l)) # second method 

p = "python"
print(type(p))  # output:- "string"


# We can change the this data types

w = 100
f = float(w)
print(type(f))   # int to float conversion

w = 100.0
f = str(w)
print(type(f))   # float to string conversion

w = 100
f = str(w)
print(type(f))  # integer to string conversion

w = "100" 
f = float(w)
print(type(f))   # string to float conversion
 
w = "100"
f = int(w)
print(type(f))  # string to float conversion

#----------------------------------------------------------------------------------------------

# Input function starts

a = input("Enter the first number:")  # 30
b = input("Enter the second number:") # 5
print(a+b)    # output:- 305, because python interprete as strings so it directly add it 

p = int(input("Enter the first number:")) # 30
q = int(input("Enter the second number:")) # 5
print(p+q)  # output :- 35, because we use int in first so python interprete as interger so they add as numerical values

k = input("Enter Your Name Here:")
l = input("Enter Your Surname Here:")
print(f"Good morning", k+l)