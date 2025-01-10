# numbers = [10,20,30,40]

# print(list(enumerate(numbers)))

# Iterative for
# for i in range(len(numbers)):
#     print(numbers[i])


# for each
# for num in numbers:
#     print(num)

# numbers = [10,20,30,40]
#
# print(dict(enumerate(numbers)))
# print(list(enumerate(numbers)))
#
# [(0,10),(1,20),(2,30),(3,40)]

# for item in enumerate(numbers):
#     index, value = item
#     print(f"index : {index}, value : {value}")

# for index, value in enumerate(numbers):
#     print(f"index : {index}, value : {value}")


my_dict = {0: 10, 1: 20, 2: 30, 3: 40}

for key, value  in my_dict.items():
    print(f"key: {key}, value: {value}")