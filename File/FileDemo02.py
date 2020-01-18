f = open('data', 'r')
line = f.readline()

while line:
    print(line, end = '')
    line = f.readline()

f.close()


filepath = 'pg57005.txt'  
with open(filepath, "r") as fp:
    i = 1
    line = fp.readline()
    while line:
        print("Line: {} {}".format(i, line.strip()))
        line = fp.readline()
        i += 1

with open(filepath, "r") as fp:
    for i, line in enumerate(fp):
        print("Line: {} {}".format(i, line.strip()))