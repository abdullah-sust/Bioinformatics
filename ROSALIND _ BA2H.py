Pattern = str(input())
dna = [[0 for i in range(100)] for i in range(100)]
for i in range(5):
	dna[i] = str(input())

def HamDis(s1,s2):
	d=0
	for i in range(len(s1)):
		if s1[i]!=s2[i]:
			d+=1
	return d
ans = 0
for i in range(5):
	dis = 10000000
	for j in range(len(dna[i])-len(Pattern)+1):
		k = HamDis(dna[i][j:j+len(Pattern)] , Pattern)
		if k<dis:
			dis=k
	ans+=dis
print(ans)
#In:
#AAA
#TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT
#Out:
#5