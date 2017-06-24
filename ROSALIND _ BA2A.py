from itertools import product
k= int(input())
d= int(input())
dna = ['ATTTGGC','TGCCTTA','CGGTATC','GAAAATT']
alpha = ['A','C','G','T']
kmer = [''.join(i) for i in product(alpha,repeat=k)]

def hamDis(s1,s2):
	p=0
	for x in range(len(s1)):
		if s1[x]!=s2[x]:
			p+=1
	return p

ans =""
for i in range(len(kmer)):
	t=0
	for j in range(len(dna)):
		mx=d+1
		for m in range(len(dna[j])-k+1):
			l=hamDis(kmer[i],dna[j][m:m+k])
			if l<=d:
				mx=l
				break
		if mx<=d:
			t=1
		else:
			t=0
			break
		if t==0:
			break
	if t==1:
		ans+=" "+kmer[i]
print (ans)
#Input:
#3 1
#ATTTGGC 
#TGCCTTA 
#CGGTATC 
#GAAAATT
#Output:
#ATA ATT GTT TTT