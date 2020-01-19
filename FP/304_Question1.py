a = [5, 7, 12, -4]


def doubleLC(lst):
    return [x * 2 for x in lst]


def doubleRec(lst):
    return [lst[0] * 2] + doubleRec(lst[1:]) if lst != [] else []


def doubleHOF(lst):
    return list(map(lambda x: x * 2, lst))


print(doubleLC(a))
print(doubleRec(a))
print(doubleHOF(a))