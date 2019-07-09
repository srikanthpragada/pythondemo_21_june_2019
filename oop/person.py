class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age


p1 = Person('Bill Gates', 63)
p2 = Person('Bill Gates', 63)

print(p1 == p2)  # p1.__eq__(p2)
print(p1)

print(p1 > p2)
