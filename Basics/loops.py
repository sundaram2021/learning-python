import time

# while loop = a statement that will run until the 
#             conditions indside it  remains true


#an infinite while loop
# while 1 == 1:
#     print("Stuck in while loop")

# name = ""

# # this while loop will run until your name's length is greater then 1
# while len(name) == 0:
#     name = input("Enter your name : ")

# print("Hello " + name)



# for loop  = a statement that will execute the code in given amount of time
#           while loop = unlimited
#           for loop = limited


# for i in range(10):
#     print(i)


# for i in range(20, 50):
#     print(i)

# for i in range(0, 51, 5):
#     print(i)

# usecase of for loop

# for i in "sundaram":
#     print(i)


# for sec in range(10, 0, -1):
#     print(sec)

#     time.sleep(1)
# print("Happy new year!!")   




# nested loops = the "inner loop" will finish all its iterations before 
#                finishing one iteration of the outer loop


# rows = int(input("Enter no. of rows : "))
# cols = int(input("Enter no. of columns : "))
# ch = input("Enter the character you want to display : ")

# for i in range(rows):
#     for j in range(cols):
#         print(ch, end="")
#     print()



# Loop control statement = change a loops execution from the normal sequence

# Break = used to terminate the loop entirely
# continue = skips to the next iterationn of the loop
# pass = does nothing , acts as a placeholder

# while True:
#     name = input("Enter your name : ");
#     if name != "":
#         break

# price = "$234"
# for i in price:
#     if i == "$":
#         continue
#     print(i, end="")


for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)