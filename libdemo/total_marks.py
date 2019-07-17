f = open("marks.txt","rt")

for line in f:  # file object is iterable
    line = line.strip("\n")  # remove newline that is at the end
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    marks = [int(m) for m in parts[1:] if m.isdigit()]  # Convert string to int in each element
    total = sum(marks)
    print(f"{name:20} {total}")

f.close()
