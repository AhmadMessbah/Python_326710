import time

# Generator

def test():
    x = 1
    print("Start Test 1")
    # load 1
    time.sleep(1)
    yield x

    print("Start Test 2")
    # load 2
    time.sleep(1)
    x += 1
    yield x

    print("Start Test 3")
    # load 3
    time.sleep(1)
    x+=1
    yield x


# my_generator = test()
#
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

for value in test():
    print(value)