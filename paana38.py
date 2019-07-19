giv1=str(input())
count=0
for n in giv1:
    if n.isnumeric() or n.isalpha():
        pass
    else:
        count+=1
print(count)
