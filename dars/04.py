def test1():
    global x
    x = 1


def test2():
    global x
    x = 2


x = 3

test1()


print(x)


# Jadid