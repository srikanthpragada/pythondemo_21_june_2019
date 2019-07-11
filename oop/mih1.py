class A:
    def process(self):
        print("Process() in A")


class B:
    def process(self):
        print("Process() in B")


class C(B):
    pass
    # def process(self):
    #     print("Process() in C")

class D(C,A):
    pass


obj = C()
obj.process()
print(C.mro())
