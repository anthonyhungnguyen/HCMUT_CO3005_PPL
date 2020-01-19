class O:
    pass


class A(O):
    def foo():
        pass


class B(O):
    pass


class C(O):
    def foo():
        pass


class D(A, B):
    pass


class E(C, A):
    pass


class F(D, E, B):
    pass


print(F.mro())
