Text='ATATCGTTTTATCGTT'
kmer={}
l=len(Text)-1
while l>-1:
	for i in range(l):
		if Text[i:i+l] not in kmer:
			kmer[Text[i:i+l]]=0
		else:
			kmer[Text[i:i+l]]+=1
	l-=1
l=max(kmer.values())
for key,val in kmer.items():
	if val==l:
		print(key)
		break
#In:
#ATATCGTTTTATCGTT
#Out:
#TATCGTT