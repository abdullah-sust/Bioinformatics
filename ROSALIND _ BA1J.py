Text=str(input())
k=int(input())
d=int(input())

from itertools import product
alpha=['A','C','G','T']
kmer = [''.join(i) for i in product(alpha, repeat= k)]
print(kmer)

#Input:
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4 1
#Output:
#GATG ATGC ATGT