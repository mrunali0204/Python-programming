#using return in function instead of print
#after return statement we do not write anything (return indicates end )

#1
def my_fun():
    return 3+4

print(my_fun())

#2
def add_num(num1,num2):
    return (num1 + num2)

print(add_num(2,3)) #here we r telling ewhat num1 and num2 is

'''
#3
def add_num():
    return (num1 + num2)

print(add_num())#here num1 and num2 is not defined nor told so error
'''

#4
num1 = input("enter num1")
num2 = input("enter num2")

def add_num():
    return (int(num1) * int(num2))#here tell taht it is int 

print(add_num())

#
name = input("tell name")

def ask_name():
    return ('welcome '+ name )

print(ask_name())


