x=int(input())
if (x%100==0):
	if(x%400==0):
		print('yes')
	else:
		print('no')
else:
	if (x%4==0):
		print('yes')
	else:
		print('no')
