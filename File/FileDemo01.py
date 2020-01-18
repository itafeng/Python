import sys

with open('data', 'r') as fp:
    line = fp.readline()
    while line:
        elements = line.strip().split(',')
        tokens = elements[0].split('||')
        print("Target Group: {}, Target: {}, Shaper: {}, rate limit: {}, timestamp: {}".format(tokens[0], tokens[1], tokens[2], elements[1], elements[2]))
        line = fp.readline()


