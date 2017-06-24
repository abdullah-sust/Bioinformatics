k = int(input())
kmer = ['CTTA','ACCA','TACC','GGCT','GCTT','TTAC']
pattern = kmer[0]
arr = [0 for i in range(len(kmer))]
l = len(kmer)+len(kmer[0])-1
i=1
arr[0]=1
while len(pattern)!=l and i<len(kmer):
	h = pattern[0:k-1]
	t = pattern[len(pattern)-k+1:len(pattern)]
	if arr[i]==0 and kmer[i][0:k-1]==t:
		pattern+=kmer[i][k-1]
		arr[i]=1
		i=1
	if arr[i]==0 and kmer[i][1:k]==h:
		pattern=kmer[i][0]+pattern
		arr[i]=1
		i=1
	i+=1
	if i==len(kmer) and len(pattern)!=l:
		i=1
print(pattern)
#In:
#4
#CTTA 
#ACCA 
#TACC 
#GGCT 
#GCTT 
#TTAC
#Out:
#GGCTTACCA
