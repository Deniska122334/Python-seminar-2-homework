N = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(N):
    x = int(input('orel(1) или reshka(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))
    
# n = int(input('Введите количество монет: '))
# count_reshka = 0
# count_orel = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_reshka += 1
#     else:
#         count_orel += 1
# if count_orel > count_reshka:
#     print(count_reshka)
# else:
#     print(count_orel)


coins = input()
orel = coins.count('1')
reshka = coins.count('0')
print(f"минимальное количество монет, которые\
нужно перевернуть: {min(orel, reshka)}")