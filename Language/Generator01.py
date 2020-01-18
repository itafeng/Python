def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

square_nums = square_numbers([1, 2, 3, 4, 5, 6])
print(square_nums)

def square_numbers_generator(nums):
    for i in nums:
        yield i * i

for n in square_numbers_generator([1, 2, 3, 4, 5, 6]):
    print(n)