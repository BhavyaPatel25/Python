dict1 = {
    1:10,
    2:20
}

dict2 = {
    3:30,
    4:40
}

dict3 = {
    5:50,
    6:60
}

# Updating dictionary 2 in dictionary 1
dict1.update(dict2)

# Updating dictionary 3 in dictionary 1
dict1.update(dict3)

# The final updated dictionary is stored in new variable
final_dict = dict1

# Final updated dictionary is printed
print(final_dict)