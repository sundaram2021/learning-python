# Functions = a block of code which is executed when it is called

# name = input("Enter your name: ");

# def hello(name, age):
#     print("hello "+ name)
#     print("You are "+ str(age) + " years old")

# hello(name)  # calling of the functions

# hello("sundaram", 21)



# return statement = Functions send python value/objects back to the caller.
#            These values/objects are known as the function's return value     

# def multiply(num1, num2):
#     res = num1 * num2;
#     return res
# x = multiply(21, 12)

# print(x)    


# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     THe order of the arguments doesn't matter, unline positional arguments
#                   Python knows the names of the arguments that our function receive

def hello(first, middle, last):
    print("Hello "+ first + " " + middle + " " + last);

# hello(last="Jha", middle = "sundaram", first="Bro")
# hello("Dude", "Sundaram", "jha")