def starts_with_upper(n):
    return n[0].isupper()


names = ['Bill', 'joe', 'Steve', 'mike']

for n in filter(lambda n: n.islower(), names):
    print(n)

for n in filter(str.islower, names):
    print(n)

for n in filter(starts_with_upper, names):
    print(n)
