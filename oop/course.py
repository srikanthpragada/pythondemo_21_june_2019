class Course:
    # Constructor
    def __init__(self, title, duration=40, fee=4000):
        # Data attributes
        self.title = title
        self.duration = duration
        self.__fee = fee  # Private attribute

    # Methods
    def print_details(self):
        print(f"Title     : {self.title}")
        print(f"Duration  : {self.duration}")
        print(f"Fee       : {self.__fee}")

    def change_fee(self, newfee):
        if newfee >= 0:
            self.__fee = newfee
        else:
            raise ValueError(f"Invalid Fee {newfee}. Fee cannot be negative!")


c1 = Course("Python", 40, 4000)  # Object
# c1.fee = 5000   # new attribute fee is created
# c1._Course__fee = 5000
c1.change_fee(-5000)
c1.print_details()

c2 = Course("Java EE", fee=5000)
c2.print_details()
