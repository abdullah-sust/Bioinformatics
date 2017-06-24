from itertools import product
k = int(input())
dna=['AAATTGACGCAT','GACGACCACGTT','CGTCAGCGCCTG','GCTGAGCACCGG','AGTACGGGACAG']
kmer =[''.join(i) for i in product(['A','C','G','T'],repeat=k)]

def hamDis(s1,s2):
	p=0
	for y in range(len(s1)):
		if s1[y]!=s2[y]:
			p+=1
	return p

def minHamDis(s,km):
	mn =k+1
	for x in range(len(s)-k+1):
		l=hamDis(s[x:x+k],km)
		if l<mn:
			mn=l
	return mn
v=10000000
ans={}
for i in range(len(kmer)):
	s=0
	for j in range(len(dna)):
		s+=minHamDis(dna[j],kmer[i])
	ans[kmer[i]]=s
	if v>s:
		v=s

for key,val in ans.items():
	if val==v:
		print(key)
		break
#In:
#3
#AAATTGACGCAT 
#GACGACCACGTT 
#CGTCAGCGCCTG 
#GCTGAGCACCGG 
#AGTACGGGACAG
#Out:
#ACG or GAC