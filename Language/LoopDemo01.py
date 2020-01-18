colors = ['red', 'blue', 'green']

print("Loop by for-in")
for color in colors:
    print(color)



print("Loop with range")
for i in range(len(colors)):
    print(colors[i])


print("Loop by index")
i = 0
while (i < len(colors)):
    print(colors[i])
    i += 1

presidents = ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Adams", "Jackson"]
for num, name in enumerate(presidents):
    print("President {}: {}".format(num, name))

ratios = [0.2, 0.5, 0.3]
for i, color in enumerate(colors):
    ratio = ratios[i]
    print("{}% {}".format(ratio * 100, color))

for color, ratio, president in zip(colors, ratios, presidents):
    print("{} {} {}".format(color, ratio, president))

for i in range(6):
    print(i, end = " ")