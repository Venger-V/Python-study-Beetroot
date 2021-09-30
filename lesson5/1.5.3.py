name = 'vitalii'
enter_name = input('Enter your name:')
enter_name_l = enter_name.lower()
name_l = name.lower()
if name_l == enter_name_l:
    print('Hi ' + enter_name_l.title())
else:
    print("It's not your name")

