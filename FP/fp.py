# from functools import reduce


# # Question 1
# def lstSquareRec(n):
#     return lstSquareRec(n - 1) + [n**2] if n > 0 else []


# def lstSquareHOF(n):
#     return list(map(lambda x: x**2, [x for x in range(1, n + 1)]))


# print(lstSquareHOF(5))


# # Question 2
# def powRec(x, n):
#     if n > 0:
#         return powRec(x, n - 1) * x
#     elif n == 0:
#         return 1
#     else:
#         return powRec(x, n + 1) * 1 / x


# def powHOF(x, n):
#     return reduce(lambda x, y: x * y, [x] * n if n > 0 else [1 / x] * (-n))


# # print(powRec(5, -5), powHOF(5, -5))

# # Question 3
# a = [1, 2, 3]
# b = [4, 5, 6]


# def listAppendRec(a, b):
#     return a if b == [] else listAppendRec(a + [b[0]], b[1:])


# def listAppendHOF(a, b):
#     return reduce(lambda x, y: x + [y], b, a)


# def reverseRec(a):
#     return [a[-1]] + reverseRec(a[:-1]) if a != [] else []


# def reverseHOF(a):
#     return reduce(lambda x, y: [y] + x, a, [])


# # Question 4
# def lessThanRec(n, lst):
#     return (
#         [lst[0]] +
#         lessThanRec(n, lst[1:]) if lst[0] < n else []) if lst != [] else []


# print(lessThanRec(50, [1, 55, 6, 2]))


# def lessThanHOF(n, lst):
#     return list(filter(lambda x: x < n, lst))


# # print(lessThanHOF(5, [1, 2, 3, 4, 5, 6, 7]))


# # Question 5
# def lookup(pattern, lst, opt):
#     return list(filter(lambda x: opt(x) == pattern, lst))


# # print(lookup('m', [('n', 3), ('m', 5)], lambda x: x[0]))

# # Tut 6.2

# # Question 1
# a = [1, 2, 3]


# # List comprehensive
# def doubleLC(lst):
#     return [x * 2 for x in lst]


# # Recursive approach
# def doubleRec(lst):
#     return [lst[0] * 2] + doubleRec(lst[1:]) if lst != [] else []


# # Higher order function
# def doubleHOF(lst):
#     return list(map(lambda x: x * 2, lst))


# # Question 2
# b = [[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.1, 3.1]]


# # List comprehension
# def flattenLC(lst):
#     return [y for x in lst for y in x]


# # Rec
# def flattenRec(lst):
#     return lst[0] + flattenRec(lst[1:]) if lst != [] else []


# # HOF
# def flattenHOF(lst):
#     return reduce(lambda x, y: x + y, lst)


# # Question 3
# def lessThanLC(n, lst):
#     return [x for x in lst if x < n]


# # print(lessThanLC(5, [1, 2, 3, 4, 5, 6, 7]))
