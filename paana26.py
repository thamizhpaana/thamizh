
a1=input()
b=a1.lstrip('-').replace('.','',1).isdigit()
if(b==True):
  print("Yes")
else:
  print("No")
