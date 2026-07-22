# # This is casual work to print 
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # Effective way :- using loops 

# for i in range(1,7):
#     print(i)

# for a in range(5,20,):
#     print(a)

# for b in range(5):  # Python intrepted as (0,5)
#     print(b)

# for c in range(0,100, 2):    #range(start, stop, step size)
#     print(c)


# # While loops

# i = 1

# while(i<8):
#     print(i)
#     i +=1

# i = 0

# while(i<8):
#     print("harry")
#     i = i + 1


# # While loop for list

# lists = [1,45690,True,"jal","lalu","kalu"]

# a = 0

# while(a<len(lists)):
#     print(lists[a])
#     a +=1


 # for loops for Lists
l = [1,2,456,78,9009]

for i in l:
    print(i)


 # for loops for Tuples
t = ("harry", 67,432,9054321)

for i in t:
    print(i)


 # for loops for Strings
s = "jal mavani"

for i in s:
    print(i)




# for loops with else 

l = [1,56,8997,9000]

for things in l:
    print(things)

else:
    print("list is over here!")  # Else work when all items,values are finished in lists,tuples,etc. 


# for loops with break and continue features
for i in range(0,25):
    print(i)
    if i==6:
        print("Completed")
        break  # Exit the loop 

for i in range(0,25):
    print(i)
    if i==6:
        print("Phase 1")
    if i==15:
        print("Phase 2")




for i in range(0,25):
    if i==20:
        continue  # Skips the value of i / iteration
    print(i)

for i in range(0,25):
    if i==20:
        print("skipped number")   # Print there where number is skipped
    if i==22:
        print("skipped another number")
        continue 
    print(i)


# extra example :- 
for i in range(4):
    print("printing")
    if i==2:
        continue
    print(i)


# pass function

for i in range(900):
    pass               # when pass used skips the whole statement/ loops

for i in range(5,15):
    print(i)

i = 0

while(i<8):
   pass
