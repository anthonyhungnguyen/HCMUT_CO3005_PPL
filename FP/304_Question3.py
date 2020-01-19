n = 50
c = [1, 55, 6, 2]


def lessThanLC(n, lst):
    return [x for x in lst if x < n]


def lessThanRec(n, lst):
    if lst != []:
        if lst[0] < n:
            return [lst[0]] + lessThanRec(n, lst[1:])
        else:
            return lessThanRec(n, lst[1:])
    else:
        return []


def lessThanHOF(n, lst):
    return list(filter(lambda x: x < n, lst))


print(lessThanLC(n, c))
print(lessThanRec(n, c))
print(lessThanHOF(n, c))