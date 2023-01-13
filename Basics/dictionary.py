# dictionary = A changeable, unorderes collection of unique key:value
#               pairs .It id fast becuase they use hashing, allow us to access
#              value quickly

capital = {
    "USA": "Wahsington DC",
    "India": "New Delhi",
    "China": "Beiging",
    "Russia": "Moscow"
}

# capital.update({"germany": "berlin"})
# capital.update({"USA ": "Las Vegas"})
# capital.pop("China")
capital.clear()

# print(capital['Guyana'])  # error
# print(capital.get("Germany"))
# print(capital.keys())
# print(capital.values())
# print(capital.items())

for key,value in capital.items():
    print(key, value)