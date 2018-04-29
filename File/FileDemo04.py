import datetime

table = {}

with open('data', 'r') as fp:
    line = fp.readline()
    while line:
        #print(line.strip())
        tokens = line.split(",")
        for index, token in enumerate(tokens):
            tokens[index] = token.strip() 
        table[tokens[0]] = tokens[1:]
        line = fp.readline()

for key, value in table.items():
    #print(value[0], value[1])
    print("Current time: ", datetime.datetime.now())
    print("Old time: ", datetime.datetime.fromtimestamp(float(value[1]) / 1000.0))
    print("Upperbound: ", datetime.datetime.fromtimestamp(float(value[1]) / 1000.0) + datetime.timedelta(0, 10))
