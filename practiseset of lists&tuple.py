# practice of lists and tuples

# Question 1 : Write a program to store seven fruits in a list entered by the user.

fruits = []

a = input("Enter fruits name:" )
fruits.append(a)
a = input("Enter fruits name:" )
fruits.append(a)
a = input("Enter fruits name:" )
fruits.append(a)
a = input("Enter fruits name:" )
fruits.append(a)
a = input("Enter fruits name:" )
fruits.append(a)
a = input("Enter fruits name:" )
fruits.append(a)

print(fruits)


# Question 2 : Write a program to accept marks of 6 students and display them in a sorted manner

marks = [90,75,35,52,36,100]
marks.sort()
print(marks) 

# another method by using input function in question 2

marks = []

m1 = input("Enter marks here:" )
marks.append(m1)
m2 = input("Enter marks here:" )
marks.append(m2)
m3 = input("Enter marks here:" )
marks.append(m3)
m4 = input("Enter marks here:" )
marks.append(m4)
m5 = input("Enter marks here:" )
marks.append(m5)
m6 = input("Enter marks here:" )
marks.append(m6)

marks.sort()
print(marks)



# Question 3 : Check that a tuple type cannot be changed in python.

a = (1, 90 , False , "harry")
a[3] = "Mavani"  # in output error shows that means tuple cannot changed in python

# Question 4 : Write a program to sum a list with 4 numbers.

l1 = [10,58,40,190]
d = sum(l1)
print(d)

# Question 5 : Write a program to count the number of zeros in the following tuple

a = (7, 0, 8, 0, 0, 9)
b = a.count(0)
print(b)






