# logical operators ( and, or, not ) = used in executing two or more conditional statement

temp = float(input("Enter the temperature : "));

# and -> both the condtions should be true
if(temp > 0 and temp <= 15):
    print("Coldie cold sshooffff..")

# or -> any one conditons should be true to execute the code
elif(temp>= 20 or temp <37):
    print("Sunny sunshine..")
    
elif not(temp < 0):
    print("Chilled cold")

else:
    print("Temp is vigourous")       