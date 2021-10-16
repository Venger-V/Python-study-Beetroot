def oops():
    raise IndexError


def oops_1():
    try:
        oops()
    except IndexError:
        print('Index Errorrrrr')


oops_1()
