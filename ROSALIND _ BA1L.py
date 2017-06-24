from itertools import product
Pattern = str(input())
alpha=['A','C','G','T']
kmer = [''.join(i) for i in product(alpha, repeat=len(Pattern))]

for i in range(len(kmer)):
	if kmer[i]==Pattern:
		print (i)
		break

#In
#AGT
#Out:
#11