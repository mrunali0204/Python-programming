#reading in file (it will return true or false)
coun_file = open("D:/Programming/reading files/countries.txt" , 'r') #in py always use / in while writing root file location
print(coun_file.readable())
coun_file.close()

'''
#reading 1st line in file

coun_file = open("countries.txt" ,"r") #here if countries.txt is not working then give whole root location of file
print(coun_file.readline()[1])
coun_file.close()

'''

#reading 1st line in file

coun_file = open("D:/Programming/reading files/countries.txt" ,"r") #here if countries.txt is not working then give whole root location of file
print(coun_file.readline()[1])
coun_file.close()



#
coun_file = open("D:/Programming/reading files/countries.txt" ,"r") #here if countries.txt is not working then give whole root location of file
for lines in coun_file.readline():
    print(lines)
coun_file.close()
