
s1 = input("Enter first string  : ")
s2 = input("Enter second string : ")

common = set()  # Empty set 
for c in s1:
    if  c in s2:
        common.add(c)


print(common)
