f = open("lists&tuple.py")
data = f.read()
print(data)
if "party" in data:
    print('ok')
else:
    print("no")
f.close()


# Write function in file I/O

name = "Rakesh Laljibhai Vanani"
f = open("rakeshfile.txt", "w")

f.write(name)
f.close()


# More file functions 

f = open("file.txt")

lines = f.readlines()  # read all lines 
print(lines, type(lines))

f.close()



f = open("file.txt")

line1 = f.readline()     # read line one by one
print(line1, type(line1))

line2 = f.readline()    
print(line2, type(line2))

line3 = f.readline()     
print(line3, type(line3))

f.close()

# Another method 

f = open("file.txt")

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()


# Some modes to open files

name = "Rakesh Laljibhai Vanani"
f = open("rakeshfile.txt", "a") # This line add in the your folder. Add everytime you run the program

f.write(name)
f.close()


# With function

# f = open("file.txt")
# print(f.read())
# f.close()    # same written as like below

with open("file.txt") as f:
    main = f.read()
    print(main)  # Due to use of with function now we not need to close file every time it cloase automatically

