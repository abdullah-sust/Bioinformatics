Text='AACGATAGCGGTAGA$'
kmer={}
order=[]
pos=[]
Text=Text+Text
l=len(Text)
c=[]
j=0
for i in range(int(len(Text)/2)):
	s=Text[int(l/2)-i:l-i]
	kmer[s]=j
	j+=1
	order+=[s]
	pos+=[j-1]
	c+=[s[0]]
	if j==(int(len(Text)/2)):
		break
n0=[]
for i in range(len(c)):
	if c[i]=='$':
		n0+=[0]
	if c[i]=='A':
		n0+=[1]
	if c[i]=='C':
		n0+=[2]
	if c[i]=='G':
		n0+=[3]
	if c[i]=='T':
		n0+=[4]

print(pos)
print(order)
print(c)
print(n0)
n1=n0
for i in range(len(n1)-1):
	j=i+1
	while j<len(n1):
		if n1[i]>n1[j]:
			t=n1[j]
			n1[j]=n1[i]
			n1[i]=t
		j+=1

ans=[]
print(n1)
for i in range(len(n1)):
	for j in range(len(n0)):
		if n1[i]==n0[j]:
			print(order[j])
			ans+=[j]
			break
print(ans)