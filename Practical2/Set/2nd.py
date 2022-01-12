set1 = {1,2,50,17,86,10}
print(set1)

# Asking the user to enter number to check whether number is there in the predefined set or not
is_there = int(input("Enter a number: "))

# If the number is in the predefined set then it will go in 'if' statement else it would go in 'else' statement.
if is_there in set1:
    set1.remove(is_there)
    print(f"{is_there} is removed")
    print(set1)
else:
    print("The number is not present in the set")