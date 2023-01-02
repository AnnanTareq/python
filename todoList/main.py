import datetime

date = {}
vls = {}
sz = 1
a = 0


print('Welcome to To-Do-List system!!!!\n')

while a<sz:
    print('1. Add \n')
    print('2. Update\n')
    print('3. Delete\n')
    print('4. Display\n')
    print('5. Search by date\n')
    print('6. Store file in txt file\n')
    print('7. Exit\n')

    print('Which service do want please press the key number as given sequence!!!!\n')
    x = int(input())

    if x == 1:
        print('How many Date do you want to add?\n')
        add = int(input())

        for i in range(add):
            dt = int(input('Enter Date'))
            mt = int(input('Enter Month'))
            yr = int(input('Enter Year'))

            key = datetime.datetime(yr, mt, dt)

            val = vls
            date[key] = vls
            for j in range(1):
                    des = input('Enter description')
                    place = input('Enter place')
                    vls[des] = place


        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break


    elif x == 2:
        up = input('Enter date to find your to-do list to update\n')
        if up in date:
            print('What do you want to update?\n')
            print('1. Date\n',date)
            print('2. Description & place \n')


            kn = int(input())
            if kn == 1:
                dt = int(input('Enter Date'))
                mt = int(input('Enter Month'))
                yr = int(input('Enter Year'))

                key = datetime.datetime(yr, mt, dt)
                date[key] = vls

            elif kn == 2:
                des = input('Enter description')
                place = input('Enter place')
                vls[des] = place
                upDict = {des: place}
                vls.update(upDict)


        else:
            break
        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break


    elif x == 3:
        kv = datetime.datetime.strptime(input('Enter a key value which you want to delete\n'))
        del date[kv]

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x == 4:
        print('All the list is here\n')
        for i in range(len(date)):
            print(date)

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x == 5:
        p = datetime.datetime(input('Enter your date to find list\n'))
        if p in date:
            print('Found!')
            print(date[p])
        else:
            print('Not Found\n')

        print('Do want to do more operation? press y\n')
        k = input()
        if k == 'y':
            sz += 1
        else:
            break

    elif x == 6:
        file = open('todolist.txt', 'w')
        file.write(str(date))
        file.close()
        print('Success\n')

    elif x == 7:
        break