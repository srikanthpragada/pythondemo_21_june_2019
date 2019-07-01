
dir = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break
    phone = input("Enter phone number :")
    if name not in dir:
        dir[name] = {phone}   # create new set with phone number
    else:
        dir[name].add(phone)  # add phone number to existing set


for name in dir:
    print(f"{name:15s} -  {' '.join(dir[name])}")


