def number():

    while True:
        try:
            a = int(input('Enter a number:\na = '))
            b = int(input('Enter a number:\nb = '))
            return print(a ** 2 / b)

        except ValueError:
            print('Both variables must be a number!\nTry again:')

        except ZeroDivisionError:
            print('Division by zero.')


number()
