# Created tuple
tuple_1 = ("Hello","my","name","is","Bhavya")
# Declaring an empty string to catch the sentence
empty_string = ""

# Running for loop and looping through each data of tuple using the variable used in for loop
# Here, used variable is 'i'
for i in tuple_1:
    # Concatenating the string looping around tuple
    empty_string=empty_string+" "+i

# Printing out the datatype of empty string after editing
print(type(empty_string))

# Printing out the new empty string after concatenation using the loop
print(empty_string)