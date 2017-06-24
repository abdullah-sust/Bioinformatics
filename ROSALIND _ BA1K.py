from itertools import product
Text = str(input())
k = int(input())

alpha = ['A','C','G','T']
kmer = [''.join(i) for i in product(alpha,repeat=k)]
arr = {}
for i in range(len(kmer)):
    arr[kmer[i]]=0

for i in range(len(Text)-k+1):
    arr[Text[i:i+k]]+=1 
ans=""
for key,val in arr.items():
    ans+=" "+str(val)
print (ans)
#In
#ACGCGGCTCTGAAA
#2
#Out:
#2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0