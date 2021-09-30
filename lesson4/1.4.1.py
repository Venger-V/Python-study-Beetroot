import random

lis = []
i = 0
while i < 10:
    lis.append(random.randint(0, 1000))
    i += 1
lis.sort()
print(lis, lis[-1], sep='>>>>')
