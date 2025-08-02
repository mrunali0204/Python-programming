
#only name and greeting
name = input("enter name")

def greeting_name():
    print('welcome ' +name )

print(greeting_name())

#name and age together (here age is in int so tell it to take into str)
name = input("enter name")
age = int(input("enter Age"))

def greeting_name():
    print('welcome ' +name + ' ur age is '+ str(age)) #here age is in int so tell it to take into str

print(greeting_name())


#ask how r u to user
def ask_cond():
    print('how are u '+name)

print(ask_cond())
 

#asking adress
address = input('address')

def address_ask():
    print('u live at '+address)

print(address_ask())#here while priniting function be aware of () otherwise error

#asking eductaion
school = input("enter ur school")
def ask_school():
    print('ur school is '+ school)

print(ask_school())

edu = input("enter edu")
def ask_edu():
    print('u r '+ edu +' educated')
print(ask_edu())




#here in functions its always returning none after output to avoid none use reutrn instead of print
school = input("enter ur school")
def ask_school():
    return('ur school is '+ school) #use return instead od print in functions



#when giving info in the print statement 
def ask_school(school,age):
    print('ur school is '+ school +' ur age is '+ str(age) )

ask_school(school = 'chris', age = 2)


#when taking input
def ask_school(school,age):
    print('ur school is '+ school +' ur age is '+ str(age) )

school = input("enter school name")
age = int(input("enter Age"))
ask_school(school, age)
