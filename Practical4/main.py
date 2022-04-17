n = int(input())

arr = map(int,input().split())
# Converting to the set helps us to remove the repeatable number from the given set
arr = list(set(list(arr)))
array_length = len(arr)
arr = sorted(arr)
print(arr[array_length-2])