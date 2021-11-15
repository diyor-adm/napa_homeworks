import math
num = int(input('Enter num: '))
if num > 0:
    print('Number sqrt = ', math.sqrt(num))
elif num < 0:
    print('Please enter positive number!')
else:
    print('Please enter another number!')
