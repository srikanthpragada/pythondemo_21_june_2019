class Marks_Iterator:
    def __init__(self,marks):
        self.marks = marks
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.marks):
            raise StopIteration
        else:
            self.pos += 1
            return self.marks[self.pos - 1]


class Marks:
    def __init__(self):
        self.marks = [20,30,40,25,66]

    def __iter__(self):
        return Marks_Iterator(self.marks)




m = Marks()
mi = iter(m)
mi2 = iter(m)

for v in m:
    print(v)

print(mi.__next__())
print(mi2.__next__())