a = 10


def fun1():
    b = 20

    def fun2():
        nonlocal  b
        b = 1
        print(a, b)

    fun2()
    print(a,b)


fun1()
