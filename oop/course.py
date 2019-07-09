class Course:
    # Class attribute or static variable
    taxrate = 14

    @staticmethod
    def change_taxrate(newtaxrate):
        Course.taxrate = newtaxrate

    # Constructor
    def __init__(self, title, duration=40, fee=4000):
        # Data attributes
        self.title = title
        self.duration = duration
        self.fee = fee  # Private attribute

    def get_fee(self):
        return self.fee + (self.fee * Course.taxrate / 100)

    # Methods
    def print_details(self):
        print(f"Title     : {self.title}")
        print(f"Duration  : {self.duration}")
        print(f"Fee       : {self.fee}")

    def change_fee(self, newfee):
        if newfee >= 0:
            self.fee = newfee
        else:
            raise ValueError(f"Invalid Fee {newfee}. Fee cannot be negative!")


if __name__ == '__main__':
    Course.change_taxrate(18)

    c1 = Course("Python", 40, 4000)  # Object
    print(c1.get_fee())
    # c1.fee = 5000   # new attribute fee is created
    # c1._Course__fee = 5000
    # c1.change_fee(-5000)
    # c1.print_details()
    #
    # c2 = Course("Java EE", fee=5000)
    # c2.print_details()
