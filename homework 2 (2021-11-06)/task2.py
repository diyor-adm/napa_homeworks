#  ============== 1-variant ===========

num = int(input('Sonni kiriting \n>>> '  ))
i , sum = 1, 0
while i <= num:
    sum += i
    i+=1
print(f'1 dan {num} gacha bo`lgan sonlar yig`indisi {sum} ga teng')

#  ============== 2-variant ===========

nums = list(range(1, int(input('Sonni kiriting: \n>>> '  ))+1))
sum = 0
for num in nums:
    sum+=num
print(f'1 dan {num} gacha bo`lgan sonlar yig`indisi {sum} ga teng')

    