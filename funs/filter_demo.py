# Should take a single value and return boolean
def iseven(n):
    return  n % 2 == 0


def isbig(n):
    return True if n > 50 else False


nums = [10, 11, 35, 55, 60, 80]

for n in filter(isbig, nums):
    print(n)
