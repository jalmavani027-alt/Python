# Question 1 :- Write a program to print multiplication table of a given number using for loop.

a = int(input("Enter a number here : "))

for i in range(1, 11):
    print(f"{a} X {i} = {a*i}")


# Question 2 :- Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if (name.startswith("S")):
        print("Hello", name)
   

# Question 3 :- Attempt problem 1 using while loop.

a = int(input("Enter a number here : "))

i =1
while(i<11):
    print(f"{a} X {i} = {a*i}")
    i +=1


# Question 4 :- Write a program to find whether a given number is prime or not.

n = int(input("Enter Number Here : "))

for i in range(2, n):
    if(n%i) == 0:
        print("This is not prime number")
        break
else:
    print("This is prime number")


# Question 5 :- Write a program to find the sum of first n natural numbers using while loop

n = int(input("Enter Number Here : "))

i= 1
sum = 0

while(i<=n):
    sum +=i
    i +=1
print(sum)       # working mechanism :- if i enter number = 6 then loops works like 0+1+2+3+4+5+6 then give the result of this sum.
                                        # but if i put condition like that while(i<n) then it works till n-1. for ex. number = 6 then 
                                        # loops works like 0+1+2+3+4+5 then give the result of this sum 


# Question 6 :- Write a program to calculate the factorial of a given number using for loop

n = int(input("Enter number here : "))
value = 1
for i in range(1, n+1):
    value = value * i
print(value)


# Question 7 :- Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3


a = "  *  "
b = " *** "
c = "*****"

print(a)
print(b)
print(c)

                        # another method

n = int(input("Enter the number : "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

# Question 8 :- Write a program to print the following star pattern:
# *
# **
# *** for n = 3

n = int(input("Enter the number : "))
for i in range(1, n+1):
    print(""* (n-i), end="")
    print("*"* (i), end="")
    print("")

                            # another method
                        
n = int(input("Enter the number : "))
for i in range(1, n+1):
    print("*"* (i), end="")
    print("")


# Question 9 :- Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *


n = int(input("Enter the number : "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")


# Question 10 :- Write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter number here : "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
