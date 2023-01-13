# exception = events detected during execution that interrupts the flow of a program

try:
    numerartor = int(input("Enter a number to divide : "));
    denominator = int(input("Enter a number to divide by: "))
    result = numerartor / denominator
except ZeroDivisionError as z:
    print(z)
    print("You cannot divide a number by 0")   
except ValueError as v:
    print(v)
    print("Try to enter only number only")     
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute")    

