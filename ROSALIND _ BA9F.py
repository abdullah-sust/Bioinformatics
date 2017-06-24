Text1='AGGGGCTCGCAGTGTAAGAA'
Text2='TCGGTAGATTGCGCCCACTC'
kmer=[]
l=1
while l<len(Text2)+1:
	for i in range(len(Text2)-l+1):
		if Text2[i:i+l] not in kmer:
			kmer+=[Text2[i:i+l]]
	l+=1

ans=0
l=1
while l<len(Text1)+1:
	for i in range(len(Text1)-l+1):
		if Text1[i:i+l] not in kmer:
			print (Text1[i:i+l])
			ans=1
			break
	if ans==1:
		break
	l+=1

#In:
#CCAAGCTGCTAGAGG 
#CATGCTGGGCTGGCT
#Out:
#AA