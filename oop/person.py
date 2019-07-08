class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Bill Gates', 63)
p2 = Person('Bill Gates', 63)

print(p1 == p2)
print(p1)