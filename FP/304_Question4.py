from functools import reduce


def composeHOF(*g):
    def h(arg):
        return reduce(lambda x, y: y(x), reversed(g), arg)

    return h


def composeRec(*lst):
    def inner(arg):
        if len(lst) == 1:
            return lst[0](arg)
        else:
            return lst[0](composeRec(*lst[1:])(arg))

    return inner


def foo(*x):
    def check(args):
        print(args)
        return 1
    return check


t = (1, 2)
foo(*t)(2)

# tuple1 = (1, 2, 3)
# print(type(*tuple1))


def double(x):
    return x * 2


def square(x):
    return x**2


def increase(x):
    return x + 1


g = composeHOF(square, increase, double)

print(g(5))
print(composeRec(square, increase, double)(5))