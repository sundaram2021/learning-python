# if statement is the block of code executed when the conditions are true


age = int(input("Enter your age : "));

if(age > 4 and age < 12):
    print("Your are a Child")
elif(age == 100):
    print("You Hit a Century.")    
elif(age < 0):
    print("You are not born yet!!")    
elif (age > 12 and age < 40):
    print("Your are an adult")
else:
    print("You are Old")        