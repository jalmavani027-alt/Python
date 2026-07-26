def user(name):
    print("Good Day", name)    # or print("Good Day" + name)

user("jal")
user("sahil")
user("het")
user("pavitra")
user("keshav")


def user(example):
    print("Good Day", example)    # or print("Good Day" + example)

user("jal")
user("sahil")
user("het")
user("pavitra")
user(1)


def user(name, ending):
    print("Good Day", name)   
    print(ending)

user("jal", "Thank you guys")
user("sahil", "Thank you guys")
user("het", "Thank you guys")
user("pavitra", "Thank you guys")
user("keshav", "Thank you guys")
print()


def user(name, words):
    print("Good Day", name)   
    print(words)

user("jal", "Thank you")
user("sahil", "Thank you")
user("het", "Thank you")
user("pavitra", "Thank you")
user("keshav", "Thank you")

print()


def user(name, words):
    print("Good Day", name)   
    print(words)
    return "it's done"

a = user("jal", "Thank you")
print(a)

print()

# default parameter value

def user(name, ending= "okay"):
    print("Good Day", name)   
    print(ending)
    return "it's done"

user("jal")
user("sahil", "thank you")
user("het")

print()


# Recursions

# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 x 2 X 1
# factorial(4) = 4 x 3 x 2 X 1
# factorial(5) = 5 X 4 x 3 x 2 X 1

# factorial(n) = n * n-1* ...... *3*2*1
# factorial(n) = n* factorial(n-1)

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter number here :"))
print("The factorial value is : ", factorial(n))

