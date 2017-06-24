k = int(input())
t = int(input())
dna = [0 for i in range(t)]
for i in range(t):
	dna[i] = str(input())
profile = [[0 for i in range(k)] for j in range(len(4))]
for i in range(t):
	for j in range(len(dna[i])):
		if dna[i][j]=='A':
			profile[0][j%k]+=1
		if dna[i][j]=='C':
			profile[1][j%k]+=1
		if dna[i][j]=='G':
			profile[2][j%k]+=1
		if dna[i][j]=='T':
			profile[3][j%k]+=1
	print(profile)
#print(dna)
