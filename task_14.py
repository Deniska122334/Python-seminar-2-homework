# N = (int(input('Введите число N ')))
# stop = 0
# P = 2
# for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end=' ')
#             P = 2
#         else:
#             stop = 1
#     else:
#         i = N

  
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i, end = ' ')
    i += 1