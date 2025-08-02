print('create ur account')

username = input('eneter username: ')
password = input('Input password: ')

print("user 'admin' created sucessfully")

print('login now')
username2 = input('input username: ')
password2 = input('input password: ')

if (username  == username2 and password == password2):
    print('user logged in sucessfully')
else:
    print('invalid ')