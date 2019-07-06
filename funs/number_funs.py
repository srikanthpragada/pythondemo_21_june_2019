def iseven(n):
    """
    Finds out whether the given number is even

    :param n: number

    :return: True if number is even otherwise false

    """
    return n % 2 == 0


def isodd(n):
    return n % 2 != 0


if __name__ == '__main__':   # running module as script
    print("Running number_funs")
else: # importing module
    print("Importing number_funs")