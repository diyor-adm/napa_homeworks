#  ============== 1-variant ===========

num = int(input('Nechchi qator ":)" chiqaramiz? \n>>> '))
smile= ':)'
i = 0
while i <num:
    print(smile)
    smile+=':)'
    i+=1 

#  ============== 2-variant ===========

num = list(range(1,int(input('Nechchi qator ":)" chiqaramiz? \n>>> '))+1))
smile= ':)'
for i in num:
    print(smile)
    smile+=':)'