myList = ['e', 'i', 'u', 'a', 'o']
print("old list: {}".format(myList))
print("new list: {}".format(sorted(myList)))

myString = 'Python'
print(sorted(myString))

myTuple = ('e', 'i', 'u', 'a', 'o')
print("old tuple: {}".format(myTuple))
print("sorted tuple: {}".format(sorted(myTuple)))
print("sorted tuple in descending order: {}".format(sorted(myTuple, reverse = True)))

# sort dictionary
myDict = {'e' : 1, 'a' : 2, 'u' : 3, 'o' : 4, 'i' : 5}
print(sorted(myDict))

# sort with key function
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

def keyFunc(elem):
    return elem[1]

sortedList = sorted(random, key = keyFunc)
print("sorted list: ", sortedList)
print("sorted list (in descending order):", sorted(random, key = lambda x:x[1], reverse = True))