#  ============== 1-variant ===========

num = int(input('Sonni kiriting \n>>> '  ))
i, sum = 0, 1
while i <= num:
    if i%2 != 0:
        sum *= i
    i+=1
print(f'0 dan {num} gacha bo`lgan barcha toq sonlar ko`paytmasi {sum} ga teng')

#  ============== 2-variant ===========

nums = list(range(1, int(input('Sonni kiriting: \n>>> '  ))+1))
sum = 1
for num in nums:
    if num%2 == 1:
        sum*=num
print(f'0 dan {num} gacha bo`lgan barcha toq sonlar ko`paytmasi {sum} ga teng')

    