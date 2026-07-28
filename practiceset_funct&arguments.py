# # Q 1 :- Write a program using functions to find greatest of three numbers.

# def greatest():
#     a = int(input("Enter value of a : "))
#     b = int(input("Enter value of b : "))
#     c = int(input("Enter value of c : "))

#     if(a>b>c):
#         print("largest number is a : ", a)
#     if(b>c>a):
#         print("largest number is b : ", b)
#     if(c>b>a):
#         print("largest number is c : ", c)

# greatest()

# # or
# a = int(input("Enter value here : "))
# b = int(input("Enter value here : "))
# c = int(input("Enter value here : "))

# def largest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c

# print("largest number is :", largest(a,b,c))

# Q 2 :- Write a python program using function to convert Celsius to Fahrenheit.

f = int(input("Enter Temperature in F: "))

def fahrenheit(f):
    return 5*(f-32)/9
c = fahrenheit(f)
print(round(c,2),"°C")

# Q 3 :- How do you prevent a python print() function to print a new line at the end.

print("a")
print("b")
print("c", end="")
print("d", end=" ")
print("e")

# Q 4 :- Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(5))

# Q 5 :- Write a python function to print first n lines of the following pattern.
# ***
# **
# *


def pattern(n):
    print("*" * n)
    print("*" * (n-1))
    print("*" * (n-2))

pattern(3)

# or


def pt(n):
    if(n==0):
        return 
    print("*" * n)
    pt(n-1)

print(pt(3))

# Q 6 :- Write a python function which converts inches to cms.

def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter inches here : "))

print("The cms value is : ", inch_to_cms(n))

# Q 7 :-  Write a python function to remove a given word from a list and strip it at the same time

def remove(lists, word):
    n = []
    for i in lists:
        if not(i==word):
            n.append(i.strip(word))
    return n

lists = ["harry","rohan",  "an", "shubhan", "rakesh"]

print(remove(lists, "an"))


# Q 8 :- Write a python function to print multiplication table of a given number

def multiply(n):
    for i in range(1, 11):
        print(n, "*" ,i, "=", (n*i))

multiply(5)
