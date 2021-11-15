num = input('Son kiriting: ')
n = int(input('Necha qatorgacha chiqaramiz? \n>>> '))
nums = ''
sum = 0
i = 0
while i<n:
    nums += num
    sum+=int(nums)
    i+=1
print(sum)