'''
#
class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)

#
class Myclass:
    x = 15
    y = 50

p1 = Myclass()
print(p1.x)
print(p1.y)

#
class Myclass:
    x = 15
    y = 50

class Theclass:
    school = 99

p1 = Myclass()
p2 = Theclass()
print(p1.x)
print(p1.y)
print(p2.school)


#
class Person:
    def __init__(self, name, age):

        self.name = name
        self.age = age
   
p1 = Person('mru', 22)
print(p1.name)
print(p1.age)


#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("enter name")
age = input("enter age")

p1 = Person(name, age)
print(p1.name)
print(p1.age)


#
class Person:
    def Persons_info(name, age):#here self is imp to tell to py for which person we are refering 
        name = name            #also in def we write __init__ (name,age) __init__ is used to intialise objects attribute
        age = age

name = input('enter name')
age = input("enter age")

p1 = Person(name, age)

print(p1.name)
print(p1.age)

#gives error bcoz of __init__ , self, self.name = name
, self.age = age not written


#correct way 
class Person:
    def __init__(self, name, age):#here self is imp to tell to py for which person we are refering 
        self.name = name            #also in def we write __init__ (name,age) __init__ is used to intialise objects attribute
        self.age = age

name = input('enter name')
age = input("enter age")

p1 = Person(name, age)

print(p1.name)
print(p1.age)
'''
'''
#
class Person:    
    def __init__(self, name, age):
        self.name = name            
        self.age = age

name = input('enter name')
age = input("enter age")

p1 = Person(name, age)

del p1
print(p1) #NAMEERROR will occur bcoz p1 is already deleated so no p1 is present 

'''

#
class Person:
    pass  # this pass will bypass error so no error

