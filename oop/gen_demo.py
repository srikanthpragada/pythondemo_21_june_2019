# Generator to yield even number from start to end
def even_numbers(start, end):
    if start % 2 != 0:
        start = start + 1

    for n in range(start, end + 1, 2):
        yield n


print(type(even_numbers(10, 20)))

for n in even_numbers(11, 21):
    print(n)


