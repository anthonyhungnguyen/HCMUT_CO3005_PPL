from functools import reduce

b = [[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.1, 3.1]]


def flattenLC(lst):
    return [single_item for single_list in lst for single_item in single_list]


def flattenRec(lst):
    return lst[0] + flattenRec(lst[1:]) if lst != [] else []


def flattenHOF(lst):
    return reduce(lambda x, y: x + y, lst)


# print(flattenLC(b))
# print(flattenRec(b))
print(flattenHOF(b))