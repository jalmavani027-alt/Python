# Now we starts strings

a = "code"   #comman string
b = '''learn code
    with me
    and my friends'''   # multi line comment


#---------------------------------------------------------------------------------------
# now go for advance level

a = "code"
print(a.capitalize())

b = "play with my friends"
print(b.replace("friends" , "family"))   # friends replace with family in output

c = "let's we play with my new friends"
print(c.upper())    # make each letters into capital alphabets

d = "THIER ARE very BEAUTIFUL FLOWERS in THAT GARDEN"
print(d.lower())   # make each letters into small alphabets


# by using input function, we get more clarity towards strings

a = input("Enter your name: ")
print(f"good morning sir" , a.upper())

b = input("Enter your surname: ")
print(f"good morning , \n {b.upper()}")   #\n for new line

c = "coding is \t best mental exercise"   #\t for tab space

k = "thier are many cricketers persent in the ceremony of world cup"
print(k.find("ceremony"))    # for find letters 

l = '''dear student
    you are selected   
    for the national exam of
    engineering'''
print(l.replace("nation" , "internation").replace("engineering" , "pharmacy")) # for multiple replace


# \n for insert new line
# \t for insert tab space
# \\ for insert backspace\




