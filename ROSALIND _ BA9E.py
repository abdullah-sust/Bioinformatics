Text1='AGGGGCTCGCAGTGTAAGAA'
Text2='TCGGTAGATTGCGCCCACTC'
kmer1=[]

l=len(Text1)
j=1
while l>0:
	for i in range(j):
		if Text1[i:i+l] not in kmer1:
			kmer1+=[Text1[i:i+l]]
	l-=1
	j+=1
ans=0
l=len(Text2)
j=1
while l>0:
	for i in range(j):
		if Text2[i:i+l] in kmer1:
			print(Text2[i:i+l])
			ans=1
			break
	if ans==1:
		break
	l-=1
	j+=1
#In:
#AGGGGCTCGCAGTGTAAGAA
#TCGGTAGATTGCGCCCACTC
#Out:
#AGA or TCG