from collections import OrderedDict

my_dictionary = OrderedDict()

for _ in range(int(input())):
    key = input()
    my_dictionary[key] = my_dictionary.get(key, 0) + 1

print(len(my_dictionary))

for key,value in my_dictionary.items():
    print(value,end = " ")