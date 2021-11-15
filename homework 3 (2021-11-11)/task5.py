text = ''
i = 1
while i<=5:
    text+='*'
    print(text)
    if len(text) == 5:
        j = 4
        while j > 0:
            print('*'*j)
            j-=1
    i+=1