with open("names.txt","wt") as f:
    names = set()
    while True:
        name = input("Enter name [end to stop] :")
        if name == 'end':
            break

        names.add(name)

    for name in sorted(names):
        f.write(name + "\n")




