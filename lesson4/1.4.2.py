import random

random.random()
lis = []
lis1 = []
i = 0
n = 0
while i == n < 10:
    lis.append(random.randint(0, 100))
    i += 1
    lis1.append(random.randint(0, 100))
    n += 1
lis3 = lis + lis1
a = set(lis3)
print(list(a))
