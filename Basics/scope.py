# scope = The region that a variable is recognized
#         A variable is only available from the inside the region it is created
#         A globaly and locally scoped versions of a variable can be created

name = "Sundaram"

def display_name():
    name = "SK"  # local scope ( available only inside a function )
    print(name)

# print(name)     # Error : name is not defined
# display_name() # SK
