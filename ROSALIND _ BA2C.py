Text = str(input())
k = int(input())
profile = [[0 for x in range(k)] for y in range(4)]
best=0
kmer=""
for i in range(4):
	for j in range(k):
		profile[i][j] = float(input())
for i in range(len(Text)-k+1):
	mul=1
	s= Text[i:i+k]
	for j in range(k):
		if s[j]=='A':
			mul*=profile[0][j]
		if s[j]=='C':
			mul*=profile[1][j]
		if s[j]=='G':
			mul*=profile[2][j]
		if s[j]=='T':
			mul*=profile[3][j]
	if mul>best:
		best=mul
		kmer=s
print(kmer)
#In:
#ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT
#5
#0.2 0.2 0.3 0.2 0.3 
#0.4 0.3 0.1 0.5 0.1 
#0.3 0.3 0.5 0.2 0.4 
#0.1 0.2 0.1 0.1 0.2
#Out:
#CCGAG