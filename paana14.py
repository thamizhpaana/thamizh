a1,b1=map(int,input().split())
for num in range(a1+1,b1):
  for i in range(2,num):
    if(num%i==0):
      break
  else:
      print(num,end=" ")
