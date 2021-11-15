#  ============== 1-variant ===========

num = int(input('Nechta son kiritasiz? \n>>> '))
sum, i = 0, 0
while i < num:
    if 0 > int(input(f'{i+1}-sonni kiriting: ')):
        sum += 1
    i += 1
if sum == 0:
    print('Kiritilgan sonlar ichida manfiy son yo`q!')
else:
    print(f'Kiritilgan sonlar ichida {sum} tasi manfiy')

#  ============== 2-variant ===========

num = int(input('Nechta son kiritasiz? \n>>> '))
i = 0
nums = []
ngt_nums = []
while i < num:
    nums.append(int(input(f'{i+1}-sonni kiriting: ')))
    if nums[i] < 0:
        ngt_nums.append(nums[i])
    i += 1
print(f'Kiritilgan {nums} sonlar ichida {len(ngt_nums)} ta manfiy son mavjud. \nBular: {ngt_nums}')
