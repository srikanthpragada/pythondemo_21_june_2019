
names = ['Bill','joe','Steve','mike']

for n in sorted(names, key=lambda  n : n.upper()):
    print(n)

for n in sorted(names, key=str.lower):
    print(n)

# sort by length of names
for n in sorted(names, key=len):
    print(n)