# Since the most occured number is referred to as the mode in statistics
# Therefore we would be importing the statistics module here

from statistics import mode

# List
list1 = [1, 51, 87, 12, 51, 8, 1, 51, 58, 96, 12, 1, 51, 87, 2, 51]
print(f"Most occured element is {mode(list1)} for {list1.count(mode(list1))} times")

# Tuple
tup = (1, 8, 9, 1, 2, 6, 7, 1, 10, 6, 5, 8, 3, 4, 1)
print(f"Most occured element is {mode(tup)} for {tup.count(mode(tup))} times")

# Dictionary
# We cannot find the most common elements as we cannot create any duplicate keys in dictionary
