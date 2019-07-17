n1,g1=map(int,input().split())
n1+=1
for v in range(n1,g1):
	i=v
	l=[]
	p=list(str(v))
	while(0<i):
		k=i%10
		l.append(k)
		i=i//10
	r=(pow(l[0],3)+pow(l[1],3)+pow(l[2],3))
	if(r==v):
		print(r,end=' ')
