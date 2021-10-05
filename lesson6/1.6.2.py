total = 0
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for i in stock:
    sum = prices.get(i, 0) * stock.get(i, 0)
    print(i.title(), sum, sep=': ')
    total += sum
print('Total amount: ', total)
