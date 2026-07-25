for i in range(1, 11, 2):
    print(i)


i=1
while(i<9):
    print(i)  
    i+=1        #out 1to8

u=5
while(u==9):
    print(u)
    i+=1         #out 1to8

i=1
while(i<9*2):
    print(i)  
    i+=1         # out 1to17

i=1
while(i<9+1):
    print(i)  
    i+=1      # out 1to9

i=1
while(i<9+1):
    print(i)  
    i+=1      # out 1to10

i=1
while(i<9):
    print(i)  
    i+=2       # out 1,3,5,7

i=1
while(i<=9):
    print(i)  
    i+=2      # out 1,3,5,7,9

i=1
while(i<9+1):
    print(i)  
    i+=1      # out 1to10
# ------------------------------------------------------------------------------------------------------------------------------------------

# using strings methods in loops 

i = 1
while(i<10):
    print("Jal Mavani", i)
    i= i+1

i = 1
while(i<10):
    a="jal mavani"
    print(i, a.upper())
    i= i+1

i = 1
while(i<10):
    a="jalmavani"
    print(i, a.capitalize())
    i= i+1

for i in range(1,11):
    k = "jalmavani"
    print(i , k.capitalize())

for i in range(1,15):
    a = "coding"
    print(a.upper(), i)


#----------------------------------------------------------------------------------------------------------------------------------------

# Using Lists & Tuples & Dictionary & Sets and Slicing in loops

l = ["harry", "hayan", False, True, 13456.12, 124054]

for i in range(1,10):
    print(i, l, "Length of this list : ", len(l))

p = ["harry", "hayan", False, True, 13456.12, 124054]

for i in p:
    print(i) 


lists = [123,453.54,True,"Doremon","Ironman"]

for i in range(10):
    print(lists[0:3])
    break


d = {
    "key" : "words",
    "harry" : "boy",
    "shilpa" : "girl",
    "king" : "male"
}

for i in range(1,5):
    print("no:-", i, ":", d)
    break

sets = {12,453,67,57890}

for i in sets:
    print(sets)
    break

for i in  range(1,5):
    print("no. :-", i, ":", sets)
    break

l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    print(l[0:6])
    break
for i in l:
    print(l[0:])
    break
for i in l:
    print(l[5])
    break

#------------------------------------------------------------------------------------------------------------------------

# Using for while in loops

for i in range(1,10):
    if(i<5):
        print("no. :-", i ,"yes")
    else:
        print("no. :-", i ,"no")


names = ["sachin", "jal", "jiya", "jayesh", "herin", "rakesh", "rohan", "sandeep"]

for i in names:
    if(i.startswith("s")):
        print("hello", i)


u = [1,2,3,4,5,6,7,10]

for i in u:
    if(sum(u)>16):
        print("sum is greater than 16")
    else:
        print("sum is lesser than 16")
    break

p = [1,2,3,4,5,6,7,10]

for i in p:
    if(max(p)>16):
        print("maximum number is greater than 16")
    else:
        print("maximum number is lesser than 16")
    break


values = []

a1 = int(input("Enter Number Here : "))
values.append(a1)
a2 = int(input("Enter Number Here : "))
values.append(a2)
a3 = int(input("Enter Number Here : "))
values.append(a3)
a4 = int(input("Enter Number Here : "))
values.append(a4)
a5 = int(input("Enter Number Here : "))
values.append(a5)

for i in values:
    print("Your input values is here : ", values)
    if(sum(values)>100):
        print("Sum is greater than 100")
        print("Sum of input number is : ", sum(values))
        print("Minimum number you input is : ", min(values))
        print("Maximum number you input is : ", max(values))

    else:
        print("Sum is lesser than 100")
        print("Sum of input number is : ", sum(values))
        print("Minimum number you input is : ", min(values))
        print("Maximum number you input is : ", max(values))  
    break

l=[]
a = int(input("Enter Number Here : "))
l.append(a)
a = int(input("Enter Number Here : "))
l.append(a)
a = int(input("Enter Number Here : "))
l.append(a)

for i in l:
    print("Your lists is here :-" , l , "Sum of number is:-" , sum(l))
    print("Min:-" , min(l))
    print("Max:-" , max(l))
    break

# --------------------------------------------------------------------------------------------------------------------------------------

                                                #  practice work 

n = int(input("Enter Number Here : "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")


lists = ["Harry", "Sohan", "Rohan", "Rishab", "Ronaldo", "Rakesh", "Swasti", "Putin"]

for names in lists:
    if(names.startswith("R")):
        print("Good Morning" , names)


n = int(input("Enter Number Here : "))
i = 1

while(i<11):
    print(f"{n} X {i} = {n*i}")
    i +=1


n = int(input("Enter Number Here : "))
i = 0

for i in range(1, n):
    if(n%2)==0:
        print("This is not prime number")
    else:
        print("This is prime number")
    break


n = int(input("Enter Number Here : "))
i = 1
sum = 0

while(i<=n):
    sum +=i
    i +=1
print(sum)


n = int(input("Enter Number Here : "))
value = 1
for i in range(1, n+1):
    value = value * i 
print(value)


n = int(input("Enter Number Here : "))
i = 1

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")


n = int(input("Enter Number Here : "))
i = 1

for i in range(1, n+1):
    print(""*(n-1), end="")
    print("*"*(i), end="")
    print("")


n = int(input("Enter the number : "))
for i in range(1, n+1):
    print("*"* (i), end="")
    print("")



n = int(input("Enter Number Here : "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")



n = int(input("Enter Number Here : "))
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")










