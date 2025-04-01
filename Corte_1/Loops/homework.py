a = input("enter a number: ")
a = int(a)
b = input("enter b number: ")
b = float(b)
c = a+b

if a == b:
    print("equal")
else:
    print("diferent")

print("type of a is: ", type(a))
print("type of b is: ", type(b))
print("c = ", c)

if type(a) == type(b):
    print("a and b are of the same type")
else:
    print("a and b are of diferent type")

