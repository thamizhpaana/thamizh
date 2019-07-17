
a1=int(input())
x=a1
sum=0
while a1>0:
    sum+=((a1%10)**3)
    a1=a1//10
if (sum==x):
    print('yes')
else:
    print('no')
