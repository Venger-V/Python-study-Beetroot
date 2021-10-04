str_ = input('Введите текст')

list_ = str_.split(' ')

dict_ = {}

for i in list_:
    if i in dict_:
        dict_[i] += 1
    else:
        dict_[i] = 1
print(dict_)
