import random

random.random()
a = []
i = 1
while i < 100:
    if i % 7 == 0 and i != 5:
        a.append(i)
    i += 1
print(a)