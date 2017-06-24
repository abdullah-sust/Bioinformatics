Pattern=str(input())
Text=str(input())
d=int(input())
#print(Pattern,Text,d)
k=len(Pattern)

def hamDis(s):
	m=0
	for i in range(len(s)):
		if s[i]!=Pattern[i]:
			m+=1
	return m

ans=""
for i in range(len(Text)-k+1):
	if(hamDis(Text[i:i+k])<=d):
		ans+=str(i)+" "
print (ans)
#Input:
#ATTCTGGA
#CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
#3
#Output:
#6 7 26 27 78