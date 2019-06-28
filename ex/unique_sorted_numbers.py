# Print all unique positive numbers in sorted order
nums = set()

while True:
    n = int(input("Enter a number :"))
    if n == 0:
        break

    if n  > 0:
        nums.add(n)


for n in sorted(nums):
    print(n)

