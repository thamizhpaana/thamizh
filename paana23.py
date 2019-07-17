g1 = int(input())
x1 = list(map(int,input().split()[:g1]))
y1 = sorted(x1)
for i in y1:
    print(i,end=" ")
