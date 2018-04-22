import sys

f = open('data', 'r')

lines = f.readlines()
for line in lines:
    print(line, end = '')
f.close()

fh = open("data1", "w")
for line in lines:
    print(line, end = '', file=fh)
fh.close

print("Hello World", file=sys.stderr)