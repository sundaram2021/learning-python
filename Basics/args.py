# * args = prarameter that will pack all arguments into a tuple
#          useful so that a functions can accept a varying amount of arguments

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum


def add(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum


print(add(1, 3, 5, 7))