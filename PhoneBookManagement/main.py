import re


Name = []
phnNumber = []
pBook = {}
pBookVal = {}
sz = 1
a = 0


print('Welcome to phonebook management system!!!!\n')

while a<sz:
    print('1. Add Person\n')
    print('2. Update\n')
    print('3. Delete\n')
    print('4. Display\n')
    print('5. Search by ID\n')
    print('6. Store file in txt file\n')
    print('7. Exit\n')

    print('Which service do want please press the key number as given sequence!!!!\n')
    x = int(input())

    if x == 1:
        print('How many person do you want to add?\n')
        add = int(input())
        for i in range(add):
            key = int(input('Enter your key number here, where your all data store...Its use as a unique id : \n'))
            val = pBookVal
            pBook[key] = pBookVal

            for j in range(1):
                fName = 'First Name'
                fNameVal = input('Enter First Name : ')
                pBookVal[fName] = fNameVal

                lName = 'Last Name'
                lNameVal = input('Enter Last Name : ')
                pBookVal[lName] = lNameVal

                address = 'Address'
                addVal = input('Enter Address : ')
                pBookVal[address] = addVal

                email = 'Email'
                emailVal = input('Enter your email : ')
                flag = 1
                it = 0
                rg = re.compile('[@]')

                if rg.search(emailVal) == None:
                    print(' @ missing\n')
                    while it < flag:
                          emailVal = input('Enter again.\n')
                          flag += 1
                else:
                     pass
                pBookVal[email] = emailVal

                phN = int(input('How many phone number do you want to add?'))
                if phN == 1:
                    phoneNumber = input("Enter your phone number here : \n")
                    phn = phnNumber.append(phoneNumber)
                else:
                    for m in range(phN):
                        print('Add phone No : ', m + 1)
                        phonenumber = input("Enter your phonenumber\n")
                        phn = phnNumber.append(phonenumber)

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x == 2:
        up = int(input('Enter key to find your contact no to update\n'))
        if up in pBook:
            print('What do you want to update?\n')
            print('1. First Name\n')
            print('2. Last Name\n')
            print('3. Address\n')
            print('4. Email\n')
            print('5. Phone\n')
            kn = int(input())
            if kn == 1:
                fName = 'First Name'
                fNameVal = input('Enter First Name : ')
                pBookVal[fName] = fNameVal
                upDict = {fName:fNameVal}
                pBookVal.update(upDict)

            elif kn == 2:
                lName = 'Last Name'
                lNameVal = input('Enter Last Name : ')
                pBookVal[lName] = lNameVal
                upDict = {lName: lNameVal}
                pBookVal.update(upDict)

            elif kn == 3:
                address = 'Address'
                addVal = input('Enter Address : ')
                pBookVal[address] = addVal
                upDict = {address: addVal}
                pBookVal.update(upDict)
            elif kn == 4:
                email = 'Email'
                emailVal = input('Enter your email : ')
                pBookVal[email] = emailVal
                upDict = {email:emailVal}
                pBookVal.update(upDict)
            elif kn == 5:
                if len(phnNumber)==1:
                    nn = input('Enter new number to update')
                    phnNumber[1] = nn
                else:
                    print('Which number do you want to update?\n')
                    k = int(input())
                    nn = input('Enter new number here')
                    phnNumber[k] = nn
        else:
            break
        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break



    elif x == 3:
        kv = int(input('Enter a key value which you want to delete\n'))
        del pBook[kv]

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x == 4:
            print('All the contacts here\n')
            for i in range(len(pBook)):

                print('Dictionary = ',pBook)

            print('Do want to do more operation? press y\n')
            k = input()
            if k == 'y':
                sz += 1
            else:
                break

    elif x == 5:
        p = int(input('Enter your key no to find contact\n'))
        if p in pBook:
            print('Found!')
            print(pBook[p])
        else:
            print('Not Found\n')

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x ==6:
        file = open('phoneBook.txt', 'w')
        file.write(str(pBook))
        file.close()

    elif x == 7:
        break