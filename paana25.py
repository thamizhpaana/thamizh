m1=int(input())
a=list(map(int,input().split()))
if(len(a)==m1):
 a.sort()
 for i in range(len(a)):
   print(a[i],end=" ") 
