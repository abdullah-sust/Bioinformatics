from itertools import product
index = int(input())
k = int(input())
alpha =['A','C','G','T']
kmer = [''.join(i) for i in product(alpha,repeat=k)]
for i in range(len(kmer)):
	if i==index:
		print (kmer[i])
		break
#Input:
#45 4
#Output:
#AGTC