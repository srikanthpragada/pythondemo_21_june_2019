
total = 0
count = 0


try:
   for i in range(1, 6):
       n = int(input("Enter number :"))
       total += n
       count += 1

except ValueError as ex:
        print("Invalid number!")





print(total / count)
