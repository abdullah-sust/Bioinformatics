from itertools import product
Pattern = str(input())
d = int(input())
alpha = ['A','C','G','T']
kmer = [''.join(i) for i in product(alpha,repeat=len(Pattern))]

def Neighbors(s1,d):
	t=0
	for i in range(len(s1)):
		if s1[i]!=Pattern[i]:
			t+=1
	if t<=d:
		print(s1)
	return

for i in range(len(kmer)):
	Neighbors(kmer[i],d)

#In:
#ACG 1
#Out:
#CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG