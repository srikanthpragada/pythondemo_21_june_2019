
nums = [90, 11, 35, 55, 60, 80]

for n in filter(lambda v : v % 2 == 0, nums):
    print(n)

for n in filter(lambda v : v % 2 != 0, nums):
    print(n)
