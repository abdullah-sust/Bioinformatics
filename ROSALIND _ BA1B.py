Text = str(input())
k= int(input())
kmer = {}
for i in range(len(Text)-k+1):
	if Text[i:i+k] not in kmer:
		kmer[Text[i:i+k]]=1
	else:
		kmer[Text[i:i+k]]+=1

m=max(kmer.values())
for key,value in kmer.items():
	if value == m:
		print (key)
#Input:
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4
#Output:
#CATG GCAT
