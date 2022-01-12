dictionary = {
    "name":"Bhavya",
    "age":"19",
    "gender":"Male"
}

# Dictionary before inserting
print(dictionary)

# Asking user to enter the weight
weight = input("Enter your weight: ")

# Inserting new key with value in the created dictionary
dictionary["weight"] = weight

# Printing out to check whether a key is inserted or not in the dictionary
print(dictionary)