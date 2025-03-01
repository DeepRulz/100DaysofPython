import sys
leng=0
if len(sys.argv[1:])> 2:
    print("Too many command-line arguments")
    sys.exit()
if len(sys.argv)<=1:
    print("Too few command-line arguments")
    sys.exit()
if sys.argv[1][-3:] !=".py":
        print("Not a Python file")
        sys.exit()
try:
    with open(sys.argv[1]) as file:
        a=file.readlines()
        for i in a:
            i=i.lstrip(" ")
            i=i.rstrip("\n")
            if len(i)==0 or i[0]=="#":
                pass
            else:
                leng+=1
except FileNotFoundError:
    print("File does not exist")
    sys.exit()
print(leng)
