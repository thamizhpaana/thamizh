num1=int(input())
sum=0
for i in range(2,num1):
    if num1%i==0:
        sum=sum+1
if sum>=1:
    print("no")
else:
    print("yes")
