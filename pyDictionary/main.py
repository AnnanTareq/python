pyBook = {}
pyDBookVal = {}
size = 1
a = 0

while a<size:
    print('1. Add\n')
    print('2. Update\n')
    print('3. Delete\n')
    print('4. Display\n')
    print('5. Search by key\n')
    print('6. Store file in txt file\n')
    print('7. Exit\n')

    print('Which service do want please press the key number as given sequence!!!!\n')
    x = int(input())

    if x == 1:
        print('How many reserve word do you want to add?\n')
        add = int(input())
        for i in range(add):
            key = input('Enter your keyword here, where your all data store...Its use as a unique id : \n')
            val = pyDBookVal
            pyBook[key] = pyDBookVal

            for j in range(1):
                des = 'Description'
                desVal = input('Enter description :')
                pyDBookVal[des] = desVal

                samCode = 'Sample Code'
                samCodeVal = input('Enter sample code :')
                pyDBookVal[samCode] = samCodeVal

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            size += 1
        else:
            break

    elif x == 2:
        up = input('Enter key to find your contact no to update \n')
        if up in pyBook:
            print('What do you want to update?\n')
            print('1. Description\n')
            print('2. Sample Code\n')
            kn = int(input())
            if kn == 1:
                desc = 'Description'
                descVal = input('Enter new description: ')
                pyDBookVal[desc] = descVal
                upDict = {desc:descVal}
                pyDBookVal.update(upDict)

            elif kn == 2:
                samCode = 'Sample Code'
                samCodeVal = input('Enter new sample code :')
                pyDBookVal[samCode] = samCodeVal
                upDict = {samCode:samCodeVal}
                pyDBookVal.update(upDict)

        else:
            break

        print('press y for more operation\n')
        k = input()
        if k == 'y':
            size += 1
        else:
            break

    elif x == 3:
        print('Delete all key-value, then press 1\n')
        j = int(input())
        if j == 1:
            kv = input('Enter a key value to delete\n')
            del pyBook[kv]
        else:
            kv = input('Enter a value from where some value you want to delete\n')
            if kv in pyBook:
                ke = input('ENter key name to delete ')
                if ke in pyDBookVal:
                    del pyDBookVal[ke]
                    print('Deleted..\n')
                else:
                    break


        print('press y for more operation\n')
        k = input()
        if k == 'y':
            size += 1
        else:
            break

    elif x == 4:
            print('Full Dictionary is here\n')
            for i in range(len(pyBook)):
                print('Dictionary = ',pyBook)

            print('press y for more operation\n')
            k = input()
            if k == 'y':
                size += 1
            else:
                break

    elif x == 5:
        p = input('Enter your key no to find reserve word\n')
        if p in pyBook:
            print('Found!')
            print(pyBook[p])
        else:
            print('Not Found\n')

        print('press y for more operation\n')
        k = input()
        if k == 'y':
            size += 1
        else:
            break

    elif x ==6:
        file = open('Dictionary.txt', 'w')
        file.write(str(pyBook))
        file.close()

    elif x == 7:
        break

