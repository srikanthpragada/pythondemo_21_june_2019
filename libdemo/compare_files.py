
f1 = open("test1.txt","rt")
f2 = open("test2.txt","rt")
s1 = f1.read()
s2 = f2.read()

if s1 == s2:
    print("Same Contents")
else:
    sl = min(len(s1),len(s2))
    lineno  = 1
    colno = 1
    for i in range(0,sl):
        if s1[i] != s2[i]:
            print(f"Differ at line {lineno} and column {colno}")
            break
        else:
            if s1[i] == '\n':
                lineno += 1
                colno = 1
            else:
                colno +=1
    else:  # files are same upto smallest file's length
        print(f"Differ at line {lineno} and column {colno}")


f1.close()
f2.close()




