# Lists can store multiple data types and elements

a = ["jal", "codewithharry", 60, 90.546, True]
print(a)

a.append("mavani")
print(a)

b = ["party", "son" , "man", 50, 50.567, False]
print(b[0:2])

print(len(b))

# Lists methods

a = ["black", "white", 90, 90.546, True]
a.reverse()
print(a)

b = [1,60,740,3452, 7, 75, 2]
b.sort()
print(b)

c = ["gym", "college", "school" , 90]
c.pop(2)
print(c)

d = [1,60,"harry",3452, "skyscapers", 75, 2]
d.insert(3, "hero")
print(d)

g = ["jal", "codewithharry", 60, 90.546, True]
g.append("coderun")
print(g)

h = ["jal", "codewithharry", 60, 90.546, True]
h.remove("codewithharry")
print(h)


# now, go towards tuples

a = (2,3,"yoyo", "hacker")
print(type(a))

b = ()
print(type(b))

# c = (1)
# print(type(c))     # output interger type not tuple

d = (1, )
print(type(d))

# now, methods of tuple

a = (2,3,"yoyo", "hacker")
b = a.index(3)
print(b)

k = (1, 50, 87, 67,90,87)
l = k.index(87)
print(l)

k = (1, 50, 87, 50, 50, 87, 50)
f = k.count(50)
print(f)

t = (1, 50, 87, 67,90,87)
print(max(t))   # give maximum valus in tuple

t = (1, 50, 87, 67,90,87)
print(min(t))   # give minimium value in tuple









