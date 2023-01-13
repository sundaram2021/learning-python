'''
**kwargs = parameter that will pack all arguments into a dictionary
           useful so that a function can accept a varying amount of
           keyboard arguments
'''

# def hello(first, last):
#     print("hello " + first + " " + last)


def hello(**kwargs):
    print("hello " + kwargs['first'] + " " + kwargs['last'])

    for key,value in kwargs.items():
        print(value, end=" ")

# hello(first="sundaram", last="jha")
hello(title = "Mr.", first="sundaram", middle="kumar", last="jha") # Error if **kwargs not used
