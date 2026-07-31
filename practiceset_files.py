# Q 1 :- Write a program to read the text from a given file ‘poems.txt’ and find out whether it
# contains the word ‘twinkle’.

file_poem = open("poems.txt")
lyrics = file_poem.read()

if ("twinkle") in lyrics:
    print("Yes twinkle word is in this file")
else:
    print("There is no word like twinkle")

file_poem.close()


# Q 2 :- The game() function in a program lets a user play a game and returns the score as an
# integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous
# Hi-score. You need to write a program to update the Hi-score whenever the game()
# function breaks the Hi-score

import random

def game():
    print("Your game is starts")
    score = random.randint(1, 100)

    with open("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print("Your Score: ", score)
    
    if(score>hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
            
    return score

game()



# Q 3 :- . Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

def generate_table(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i} \n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

for i in range(2, 21):
    generate_table(i)



# Q 4 :-. A file contains a word “Donkey” multiple times. You need to write a program which
# replaces this word with ##### by updating the same file.

f = open("multiply.txt")
word = f.read()

if ("donkey" in word):
    a = word.replace("donkey", "######")
    print(a)
else:
    print("nothing")

f = open("multiply.txt", "w")
f.write(a)

f.close()


# Another methods


word = "donkey"

with open("multiply.txt") as f:
    content = f.read()

content_change = content.replace(word, "######")

with open ("multiply.txt", "w") as f:
    f.write(content_change)



# Q 5 :- Repeat program 4 for a list of such words to be censored.

lists = ["donkey", "monkey", "weird", "fool", "bad", "pagallll"]
 
with open("multiply.txt") as f:
    content = f.read()

for word in lists:
    content = content.replace(word, "#" *  len(word))

with open ("multiply.txt", "w") as f:
    f.write(content)



# Q 6 :- Write a program to mine a log file and find out whether it contains ‘python’.

f = open("log.txt")
datas = f.read()

if ("python" in datas or "Python" in datas):
    print("Yes, python word in included in this particular files")
else:
    print("Thier is no words like python in this particular files")

f.close()



# Q 7 :- Write a program to find out the line number where python is present from ques 6

f = open("log.txt")

line1 = f.readline()
print(line1)
if ("python" in line1):
    print("python word found in first line")
else:
    print("Python word not in first line")

line2 = f.readline()
if ("python" in line2):
    print("python word found in second line")
else:
    print("Python word not in second line")

line3 = f.readline()
if ("python" in line3):
    print("python word found in third line")
else:
    print("Python word not in third line")

f.close()



# Q 8 :- Write a program to make a copy of a text file “this.txt”.

f = open("this.txt")
content_in_f = f.read()

f = open("sp.txt", "w")
g = f.write(content_in_f)

f.close()


# Q 9 :- Write a program to find out whether a file is identical and matches the content of another file.

with open("this.txt") as f:
    content1  = f.read()

with open("sp.txt") as f:
    content2 = f.read()

if (content1 == content2):
    print("Yes, both files are identical")
else:
    print("No, both files are not identical")



# Q 10 :- Write a program to wipe out the content of a file using python.
 
with open("poems.txt", "w") as f:
    f.write("")


# Another method


f = open("poems.txt", "w")
f.write("")

f.close()



# Q 11 :- Write a python program to rename a file to “renamed_by_python.txt”.

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt" , "w") as f:
    f.write(content)


# Another method 


import os

# Old file name
old_name = "old.txt"

# New file name
new_name = "renamed_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print("File renamed successfully.")