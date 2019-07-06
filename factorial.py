
# Factorial

import sys

if len(sys.argv) < 2:
    print("Missing number!")
    sys.exit(0)   # Stop program

num = int(sys.argv[1])

fact = 1
for i in range(2,num + 1):
    fact *= i

print(f"Factorial of {num} is {fact}")