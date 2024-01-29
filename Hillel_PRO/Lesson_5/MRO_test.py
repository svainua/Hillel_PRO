# class A:
#     pass


# class B(A):
#     pass


# class C(A):
#     pass


# class D(B, C):
#     pass


# print(D.mro())


class O:
    pass


class A(O):
    pass


class B(O):
    pass


class C(O):
    pass


class D(O):
    pass


class E(O):
    pass


class K1(A, B, C):
    pass


class K2(B, D):
    pass


class K3(C, D, E):
    pass


class Z(K1, K2, K3):
    pass


def print_mro(class_name):
    print(*[item.__name__ for item in class_name.mro()], sep=" --> ")


print_mro(Z)
