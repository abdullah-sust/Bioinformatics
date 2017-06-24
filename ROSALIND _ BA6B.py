P=[3,4,5,-12,-8,-7,-6,1,2,10,9,-11,13,14]
brPoint=0
P=[0]+P
P=P+[len(P)]
for i in range(len(P)-1):
	if (P[i+1]-P[i])==1:
		;
	else:
		brPoint+=1
print(brPoint)