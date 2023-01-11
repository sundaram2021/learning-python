# variables => a container for a value. Behaves as the value that it contains

#here we have used string datatype

# here 'Sundaram' is value that is assigned to name variable
# first_name = "Sundaram" 
# last_name = "Jha"
# full_name = first_name+ " " + last_name

# print the datatype of the name variable
# print(type(full_name)) 

# this is hoe you display output to the user
# print("Hello " + full_name) 


#here we will use int datatype
# age = 21;
# age += 1;

# print(type(age))

#you cannot perform concatination with int datatype in python
#print("Your age is : " + age);

# you have to use str() method to convert int to string datatype
# print("Your age is : " + str(age));



#Here we will use float datatype

#we can store decimal numbers in float datatype
# length = 12.455
# print("your height is : " + str(length))
# print(type(length)) 


#Boolean Datatype => we can store true or false value int this datatype

# late = False
# print("Are you late - " + str(late));
# print(type(late))


#----------------------------------------------------



#######################################################
''' 
Multiple assignment in python
=> allows us to assign multiple
   variables at the same time in 
   one line of code

'''
#this is how you can assign multiple variable in one line of code
name, age, attractive = "sundaram", 20, True;

print(name, age, attractive);

#if multiple variable have same value

sandy = manny = tuna = liya = 30;
