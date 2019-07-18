xxz=input()
hh=xxz.strip()
ddz=1
for i in range (len(hh)):
    if(hh[i]==' ' and (hh[i]!=hh[i+1])):
        ddz=ddz+1
if(ddz>1):
    print(ddz)
