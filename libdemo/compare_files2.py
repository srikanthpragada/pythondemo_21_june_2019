
f1 = open("test1.txt","rt")
f2 = open("test2.txt","rt")

lineno = 1
while True:
    line1 = f1.readline()
    line2 = f1.readline()
    if line1 == "" and line2 == "":
        print("Same Content")
        break
    







f1.close()
f2.close()




