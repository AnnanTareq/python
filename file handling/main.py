# f = open('demofile.txt','w')

# f = open('demofile.txt','r')
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# fh = open('demofile.txt','a')
# fh.write('Now this line has been added after creating')
#
# fh = open('demofile.txt','r')
# print(fh.read())


"""

Create new file

"""

# f1 = open('Tareq.txt','x')
# f1 = open('Tareq.txt','w')
# f1.write('My name is Tareq and I am a graduate student.')
# f1 = open('Tareq.txt','r')
# print(f1.read())
#
# """
#     Add new line in existing file
# """
#
# f2 = open('Tareq.txt','a')
# f2.write('Hopefully I will be go to abroad soon, for study purpose')
# f2 = open('Tareq.txt','r')
# # print(f2.read())
#
# for i in f2:
#     print(i)
#
# f2 = open('Tareq.txt','w')
# f2.write('I am Tareq who is a computer engineer')
# f2 = open('Tareq.txt','r')
# print(f2.read())

"""
import os

os.remove('Tareq.txt')
"""

# f3 = open('joy','x')
#
# import os
# os.remove('joy')
#
#

# f5 = open('TareqAnnan.csv','x')
# f5 = open('TareqAnnan.csv','w')
# f5.write('Name')
# f5.close()
#
# f6 = open('TareqAnnan.csv','r')
# f6.read()

#
# import os
#
# if os.path.exists('TareqAnna.csv'):
#     print('File exist here')
# else:
#     print("File doesn't exist")


"""
    Read write CSV file
"""

import csv


# header = ['Name','Age','email','Phone']
# data = ['Masum',25,'masum@gmail.com','019191919']
#
# f = open('TareqAnnan.csv','w')
#
# wr = csv.writer(f)
#
# wr.writerow(header)
# wr.writerow(data)

# f7 = open('TareqAnnan.csv','r')
# print(f7.read())

inp = input('ENter your desired value')
print(type(inp))
typeCast = int(inp)
print(type(typeCast))
for i in range(typeCast):
    print(i)
