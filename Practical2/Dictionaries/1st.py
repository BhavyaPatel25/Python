# Create a dictionary
dictionary = {
    "name":"Bhavya",
    "age":"19",
    "roll_no":"20CE079"
}

# Entering the work to check if key exist in given dictionary
key_to_be = input("Enter the key you want to check: ")

# If the key entered is in dictionary it would go in if block and print the following statement
if key_to_be in dictionary.keys():
    print("Key is present in the given dictionary")
else:
    print("Key is not there")