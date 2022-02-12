for i in range(int(input())):
    s =input()
    l = len(s)
    mid = int(l / 2)
    if(l%2==0):
        str1 = s[:mid]
        str2 = s[mid:]
    else:
        str1 = s[:mid]
        str2 = s[mid+1:]
    lt1 = list(str1)
    lt2 = list(str2)
    lt1.sort()
    lt2.sort()

    if(lt1==lt2):
        print("YES")
    else:
        print("NO")