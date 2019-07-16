N1,K1=map(int,input().split())
arrq=[]
j=N1
m=1
arrq=[int(i)for i in input().split()]
sum=0
i=0
while K1>0:
  sum+=arrq[i]
  K1=K1-1
  i=i+1
print(sum)
