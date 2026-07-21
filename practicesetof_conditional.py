# # Question 1 : Write a program to find the greatest of four numbers entered by the user.

# a1 = int(input("Enter number 1 :"))
# a2 = int(input("Enter number 2 :"))
# a3 = int(input("Enter number 3 :"))
# a4 = int(input("Enter number 4 :"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1 is greatest number among all the numbers : ", a1)
# if(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greatest number among all the numbers : ", a2)
# if(a3>a1 and a3>a2 and a3>a4):
#     print("a3 is greatest number among all the numbers : ", a3)
# if(a4>a1 and a4>a2 and a4>a3):
#     print("a4 is greatest number among all the numbers : ", a4)

# # Or 

# a1 = int(input("Enter number 1 :"))
# a2 = int(input("Enter number 2 :"))
# a3 = int(input("Enter number 3 :"))
# a4 = int(input("Enter number 4 :"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("a1 is greatest number among all the numbers : ", a1)
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("a2 is greatest number among all the numbers : ", a2)
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("a3 is greatest number among all the numbers : ", a3)
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("a4 is greatest number among all the numbers : ", a4)

# # or

# a1 = int(input("Enter number 1 :"))
# a2 = int(input("Enter number 2 :"))
# a3 = int(input("Enter number 3 :"))
# a4 = int(input("Enter number 4 :"))

# greatest = max(a1,a2,a3,a4)
# print("This is greatest number among all other input numbers : " , greatest)


# # Question 2 : Write a program to find out whether a student has passed or failed if it requires a total of
# # 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# # input from the user.

# marks1 = int(input("Enter your 1st subject marks :"))
# marks2 = int(input("Enter your 2nd subject marks :"))
# marks3 = int(input("Enter your 3rd subject marks :"))

# # now we check total percentage

# total_percentage = (100*(marks1 + marks2 + marks3))/300

# if(total_percentage>40, marks1>=33 and marks2>=33 and marks3>=33):
#     print("Congratulations you are pass : ", total_percentage )

# else:
#     ("You are fail")


# Question 3 : A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.


spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

user = input("Enter you comment here : ")

if((spam1 in user) or (spam2 in user) or (spam3 in user) or (spam4 in user)):
    print("This is spam comment. Be aware !")

else:
    print("This is safe comment")



# Question 4 : Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter Your Username Here : ")
len_username = len(username)

if(len_username<=10):
    print("Less than 10 characters : ", len(username))

else:
    print("greater than 10 characters : ", len(username))


# Question 5 : Write a program which finds out whether a given name is present in a list or not.

l1 = []

name1 = input("Enter Your Name Here : ")
l1.append(name1)
name2 = input("Enter Your Name Here : ")
l1.append(name2)
name3 = input("Enter Your Name Here : ")
l1.append(name3)
name4 = input("Enter Your Name Here : ")
l1.append(name4)
name5 = input("Enter Your Name Here : ")
l1.append(name5)

print(l1)

l2 = ["jal", "het", "aryan", "jeel", "sahil"]

if((name1 in l2) and (name2 in l2) and (name3 in l2) and (name4 in l2) and (name5 in l2)):
    print("Congrats Your Name Is Included In This List")

else:
    print("Sorry Your Name Is Not In List")


# Question 6 :  Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

student_grade = int(input("Enter Your Marks Here : "))

if(90<=student_grade<=100):
    print("Excellent performance")

elif(80<=student_grade<90):
    print("A grade")

elif(70<=student_grade<80):
    print("B grade")

elif(60<=student_grade<70):
    print("C grade")

elif(50<=student_grade<60):
    print("D grade")

elif(student_grade<=50):
    print("Fail")


# Question 6 : Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Type Your Post Here : ")

word5 = "harry"

if(word5 in post):
    print("Yes, harry word is in this post")

else:
    print("No words related to harry is available in this post")


    

