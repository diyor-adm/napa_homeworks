text = input('Matn kiriting: ')
i = 0
sum = 0
while i < len(text):
    if text[i] == 'p' or text[i] =='P':
        sum += 1
    i += 1
print(sum)

# =============

text = input('Matn kiriting: ')
sum = 0
for letter in text:
    if letter == 'p' or letter =='P':
        sum += 1
print(sum)