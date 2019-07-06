import sys

# copy string from sys.argv to a list of int

nums = set()
for v in sys.argv[1:]:
    nums.add( int(v) )

min_num = min(nums)  # smallest of given numbers

factors = []

for i in range(2, min_num//2 + 1):
    for n in nums:
        if n % i != 0:
            break
    else: # i is a factor for all numbers
        factors.append(i)


print(factors)