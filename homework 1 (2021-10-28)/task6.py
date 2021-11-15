num1 = int(input('Enter 1st num: '))
num2 = int(input('Enter 2nd num: '))
num3 = int(input('Enter 3rd num: '))
num4 = int(input('Enter 4th num: '))
ngt_nums = 0
if num1 < 0:
    ngt_nums = ngt_nums+1
if num2 < 0:
    ngt_nums = ngt_nums+1
if num3 < 0:
    ngt_nums = ngt_nums+1
if num4 < 0:
    ngt_nums = ngt_nums+1

if ngt_nums > 0:
    print(ngt_nums, 'negative number(s)')
else:
    print('There is no negative number!')
