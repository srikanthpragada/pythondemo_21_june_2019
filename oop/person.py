class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age


class Student(Person):
    def __init__(self, name, age, course):
        # super().__init__(name,age)
        Person.__init__(self, name, age)
        self.course = course

    def __str__(self):
        return f"{super().__str__()} - {self.course}"


p1 = Person('Bill Gates', 63)
s1 = Student('Mike', 23, "MS CS")

print(s1)

print(issubclass(Student, Person))
print(issubclass(Student, object))
