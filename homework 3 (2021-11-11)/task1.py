nums = int(input('Nechta sonni o`rta arifmetigini hisloblaymiz?\n>>>'))
i = 1
sum = 0
while i <= nums:
    num = int(input(f'{i}-sonni kiritng: '))
    sum += num
    i += 1
print(f'Kiritilgan {nums} sonning o`rta arifmetigi {sum/nums} ga teng.')
