def mathoper(oper, n1, n2):
    print(oper(n1, n2))


def add(n1, n2):
    return n1 + n2


def mul(n1, n2):
    return n1 * n2


mathoper(add, 10, 20)
mathoper(mul, 10, 20)
