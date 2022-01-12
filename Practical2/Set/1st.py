set1 = {1,2,3}

# Asking user to input a number to be added in the set
add_member = int(input("Enter an integer you want of add in set: "))

# The entered number is added to the set
set1.add(add_member)

# After adding
print(set1)

# Set declared is clear.Therefore, there are no elements in the set right now
set1.clear()

# Empty set gets printed
print(set1)