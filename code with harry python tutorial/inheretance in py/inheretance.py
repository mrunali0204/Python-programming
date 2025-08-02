'''
#it means taking from existing class and engaging methods and everything &N putting it  in new class

from try_file import student

class person(student):
    pass

p1 = person()
print(p1.name)
#here error occured bcoz in samll letters written student (correct way 'S'tudent)
'''
'''
#correct way with no error 
from try_file2 import Student

class person(Student):
    pass

p1 = person()
print(p1.name)
'''

from try_file2 import Student
