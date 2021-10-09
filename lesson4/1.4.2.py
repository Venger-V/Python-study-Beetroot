import random

lis = []
lis1 = []
i = 0
n = 0
#  увеличил списки, с n < 10 lis2 может быть пустым
while i == n < 20:
    lis.append(random.randint(0, 100))
    i += 1
    lis1.append(random.randint(0, 100))
    n += 1
lis2 = list(set(lis) & set(lis1))
print(lis2)
