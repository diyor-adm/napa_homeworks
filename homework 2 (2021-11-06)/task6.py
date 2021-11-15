num = int(input('Son kiriting: '))
i = 2
isCompound = False
if num < 2:
    print('Xato')
while i < num/2:
    if num % i == 0:
        print('Murakkab son')
        isCompound = True
        break
    i += 1
if not(isCompound):
    print('Tub son')


