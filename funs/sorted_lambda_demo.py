
nums = [-20, 11, 3, 55, 5, 60, -80]

for n in sorted(nums,key=lambda n : abs(n)):
    print(n)

for n in sorted(nums,key=abs):
    print(n)
