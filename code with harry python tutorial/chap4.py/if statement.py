'''
#for 2 no.s

a = input("enter a")
b = input("enter b")

if a>b:
    print("a>b")

else:
    print("b>a")

#for 3 no.s

a = input("enter a")
b = input("enter b")
c = input("enter c")

if a>b>c:
    print("a>b&c")

elif b>a>c:
    print("b>a&c")


else:
    print("c>a&b")


#checking above 18 or not
age = int(input("enter age"))

if age > 18:
    print("ok")

else:
    print("not ok")


#

harshu = int(input("enter harshus age"))
if harshu > 10:
    print("gooooddd")


#even or odd

n = int(input("enter n"))
if n%2==0:
    print("even")

else:
    print("odd")

'''
#checking if value is str or int without type(value)
value = input("enter value ")
if type == str: #need to write type(value) means [type of whome] if only this (type == str) it will print int always
    print("str")
else:
    print("int")

#checking if value is str or int with type(value)
value = input("enter value ")
if type(value) == str: #need to write type(value) means [type of whome] if only this (type == str) it will print int always
    print("str")
else:
    print("int")