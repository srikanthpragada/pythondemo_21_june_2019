import os
import sys


def print_file(filename):
    with open(filename) as f:
        print("\n\n" + filename)
        print('-' * len(filename))
        for (lineno, line) in enumerate(f, start=1):
            print(f"{lineno:03}: {line}", end='')


if len(sys.argv) > 1:
    root = sys.argv[1]
else:
    root = r"e:\classroom\python\june21\pythondemo"

allfiles = os.walk(root)

for (dirname, dirs, files) in allfiles:
    if dirname.find(".git") >= 0:
        continue

    for file in files:
        if file.endswith(".py"):
            print_file(dirname + "\\" + file)
