P=[-3,4,1,5,-2]
current=1
fele=0
start=0
end=0
temp=[]

for i in range(len(P)):
	if abs(P[i])==current:
		fele+=1
		temp+=[-P[i]]
		t=len(temp)
		m=start
		while t>start:
			P[m]=temp[t-1]
			#print(temp[t-1])
			m+=1
			t-=1
		print(P)
		while P[start]>0:
		current+=1
		fele=0
		temp=[]
	else:
		end+=1
		fele+=1
		temp+=[-P[i]]
