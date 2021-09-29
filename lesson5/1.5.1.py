a = input(str('Enter a text:'))
if len(str(a)) < 2:
    print('')
else:
    b = str(a[:2]) + str(a[-2:])
    print(b)
