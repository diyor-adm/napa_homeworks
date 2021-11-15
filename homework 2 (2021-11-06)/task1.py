#  ============== 1-variant ===========

num = int(input('Nechchini kvadratigacha hisoblaymiz? \n>>> '  ))
i = 1
while i<=num:
    print(f'{i} ning kvadrati {i**2} ga teng')
    i+=1

#  ============== 2-variant ===========

nums = list(range(1, int(input('Nechchini kvadratigacha hisoblaymiz? \n>>> '  ))+1))
for num in nums:
    print(f'{num} ning kvadrati {num**2} ga teng')
