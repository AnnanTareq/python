import os
import csv

print('Welcome to Charity Page')

print('Where do you want to go?')
print('1. Sign up')
print('2. Log In')
print('3. Donate')

a = input('Input your desired option number')

try:
    databaseSearch = open('Database.csv','r')
    databaseSearch.close()
except:
    csvDatabase = open('Database.csv','x')
    csvDatabase.close()
finally:
    header = ['Name', 'Age', 'Email', 'Phone', 'Address', 'Password']
    csvDatabase1 = open('Database.csv', 'w')
    head = csv.writer(csvDatabase1)
    head.writerow(header)


if a == '1':

    usr = input('If you are admin, then press "y" otherwise "n" ')
    if usr == 'y':
        usrN = input('How many user do you want to register?')
        ran = int(usrN)
        for i in range(ran):
            name = input('Enter your Name here')
            age = input('Enter your age here')
            email = input('Enter your Email address here')
            phone = input('Enter your phone number here')
            address = input('Enter your address here')
            password = input('Enter your password here')


    else:
        print('User page')


