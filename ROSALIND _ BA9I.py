Text='GCGTGCCTGGTCA$'
order=[]
pos=[]
Text=Text+Text
l=len(Text)
j=0

for i in range(int(len(Text)/2)):
	s=Text[int(l/2)-i-1:l-i-1]
	order+=[s]
	pos+=[j]
	j+=1
	if j==(int(len(Text)/2)):
		break
n=[]
for i in range(len(order)):
	if order[i][0]=='$':
		n+=[0]
	if order[i][0]=='A':
		n+=[1]
	if order[i][0]=='C':
		n+=[2]
	if order[i][0]=='G':
		n+=[3]
	if order[i][0]=='T':
		n+=[4]
p=int(len(Text)/2)
ans=order[0][p-1]
for i in range(len(order)):
	if order[i][0]=='A':
		ans+=order[i][p-1]
for i in range(len(order)):
	if order[i][0]=='C':
		ans+=order[i][p-1]
for i in range(len(order)):
	if order[i][0]=='G':
		ans+=order[i][p-1]
for i in range(len(order)):
	if order[i][0]=='T':
		ans+=order[i][p-1]
print(ans)
#ACTGGCT$TGCGGC