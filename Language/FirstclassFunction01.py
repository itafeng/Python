def square(x):
    return x * x

f = square
print(f)
print(f(5))

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)