n = int(input())

families = map(int, input().split())
families = sorted(families)

for i in range(len(families)):
    if(i!=len(families)-1):
        if(families[i]!=families[i - 1] and families[i]!=families[i + 1]):
            print(families[i])
            break
    else:
        print(families[i])