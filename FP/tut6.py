from functools import reduce

# Q4


def composeHOF(*function):
    def h(args):
        return reduce(lambda x, y: y(x), reversed(g), args)

    return h


def double(x):
    return x * 2


def square(x):
    return x**2


def increase(x):
    return x + 1


print(composeHOF(square, increase, double)(5))
