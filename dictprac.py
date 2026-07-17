# Dictionary & Sets practice

Age = {
    "Rohan" : 18,
    "Rakesh": 17,
    "Mahesh" : 20,
    "Rahul" : 25
}

print(Age)
print(type(Age))

# Methods Of Dictionary

Age = {
    "Rohan" : 18,
    "Rakesh": 17,
    "Mahesh" : 20,
    "Rahul" : 25
}
Age.copy()
print(Age)

Age.pop("Rohan")
print(Age)

C = Age.get("Rakesh")
print(C)

print(Age["Rakesh"])
print(Age.items())
print(Age.keys())
print(Age.values())

Age.update({"Jal" : 20})
print(Age)

