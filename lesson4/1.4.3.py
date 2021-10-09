list_ = []
i = 1
while i < 100:
    if i % 7 == 0 and i % 5 != 0:
        list_.append(i)
    i += 1
print(list_)

