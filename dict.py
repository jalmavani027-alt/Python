# # dictionary

# d = {} # This is empty dictionary

# marks = {
#     "Jal" : 180,
#     "Harry" : 100,
#     "Het" : 50,
#     "Roshan" : 10
# }
# print(type(marks), marks)

# print(marks["Jal"])
# print(marks["Harry"])  

# a = {
#     "value" : "valueaccess",
#     "code" : "coding",
#     "digits" : [1,565,532,5,6.075]
# } 

# print(a["digits"])


# # Methods of Dictionary

# b = {
#     "Harry" : 100,
#     "Jal" : 190,
#     "Jeel" : 170,
#     "Priyank" : 105,
#     170 : "Guddu"
# }
# print(b.items())
# print(b.keys())
# print(b.values())

# b.update({"Jeel" : 175 , "Ajay" : 150})
# print(b)

# print(b.get("Jal")) # return values correponding to their keys word
# print(b.get("Rakesh")) # return none 

# # check difference
# print(b.get("Jal10"))  # returns none
# # print(b["Jal10"])  # returns an error

# print(b.popitem())
# print(b.pop("Harry"))
# k = len(b)
# print(k)


# #---------------------------------------------------------------------------------------------------------------------------------------
 
# # Sets starts

# s = {1,45,2321} # This is set
# print(s)

# a = set() # This is empty set
# print(type(a))

# b = {10,45,32,22,10,10,10}  # repition is not allowed (only 1 time 10 comes in output)
# print(b, type(b))           # Sets is unordered



# Methods/ Operation in Sets

c = {1, 34,657,678,10, 125830}

c.add(1078)
print(c)

print(len(c))

c.remove(34)
print(c)

# c.clear()
# print(c)

c.copy()
print(c)

# union and intersection 

s1 = {1,45,65,54,90}
s2 = {1,65,78,64,33,50,98,80,95}

print(s1.union(s2))
print(s1.intersection(s2))

a = s2-s1
print(a)
t = s1-s2 
print(t)

s3 = {1,2,3,4,5}
s4 = {1,4,2,90,5678}

b = s3-s4
print(b)
c = s4-s3
print(c)

d = {1,2,3}
g = {1,2,3}
k = g - d
print(k)   # returs set()







