# Cannot change actual parameter through formal parameter as object is immutable
def change(n):
    print(id(n))
    n = 0
    print(id(n))


# Can change actual parameter through formal parameter as object is mutable
def add_to_end(lst, v):
    lst.append(v)


a = 100
print(id(a))
change(a)
print(id(a))
print(a)

l = [10, 20]
add_to_end(l, 30)
print(l)
