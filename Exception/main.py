# try:
#     print(x)
# except:
#     print('An exception occurred')

#
# try:
#     print(x)
# except NameError:
#     print('Variable x is not defined')
# except:
#     print('Something else went wrong')
#
"""Use ELse block"""
#
# try:
#     print(r)
# except:
#     print('Something went wrong')
# else:
#     print('Nothing went wrong')

"""use Finally """
#
# try:
#     print(x)
# except:
#     print('SOmething went wrong')
# finally:
#     print('The try except is finished')

"""nested try except block"""

try:
    f = open('NewFile.txt','r')
    print('Printed from first try block :',f.read())
except:
    f = open('NewFile.txt','x')
    try:
        f = open('NewFile.txt','w')
        f.write('This is a new file, created inside nested try except block')
        f.close()
    finally:
        f = open('NewFile.txt','r')
        print('Print from finally block',f.read())

