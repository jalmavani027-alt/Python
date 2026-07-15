# Lists & Tuples practice starts from here

list = ["code", "coding", "kangaroo", "monkey", 90, False, 90.234, 70.90]
a = len(list)
print(a)

b =list.count("code")
print(b)

c = list[0:3]
print(c)
        #or
print(list[1:4])

list.append("mango")
print(list)

# list.clear()
# print(list)  # remove all data types from the list

# list.copy()
# print(list)  # give copy of list

list.index("kangaroo")
print(list)

list.insert(3, 90234)
print(list)

list.pop(3)
print(list)

list.remove("kangaroo")
print(list)

list.reverse()
print(list)


l1 = [1,23,564,3,21,22,223,12,41,11,100]
print(type(l1))  # type list

l1 = (1,23,564,3,21,22,223,12,41,11,100)
print(type(l1))  # type tuple


age = []
a = input("Enter your age here:")
age.append(a)
a = input("Enter your age here:")
age.append(a)
a = input("Enter your age here:")
age.append(a)
a = input("Enter your age here:")
age.append(a)
a = input("Enter your age here:")
age.append(a)

age.count(50)
print(age)


# tuple starts

a = ("mango", "monkey", "apple" , "aeroplane" , 80 , True)
print(type(a))

t1 = a.index("monkey")
print(t1)  # give the exact location of value

t2 = a.count("mango")
print(t2)

b = (1, 70,8540,28424,21)
print(min(b))
print(max(b))




