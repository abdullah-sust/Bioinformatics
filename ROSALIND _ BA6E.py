k=int(input())
s1=str(input())
s2=str(input())

kmer1=[]
kmer2=[]
rev=[]
for i in range(len(s1)-k+1):
	kmer1+=[s1[i:i+k]]
for i in range(len(s2)-k+1):
	kmer2+=[s2[i:i+k]]
	s=""
	s2[i:i+k]
	l=len(s2[i:i+k])-1
	x=0
	while l>-1:
		if s2[i:i+k][l]=='A':
			s+="T"
		if s2[i:i+k][l]=='T':
			s+="A"
		if s2[i:i+k][l]=='G':
			s+="C"
		if s2[i:i+k][l]=='C':
			s+="G"
		l-=1
	rev+=[s]


for i in range(len(kmer1)):
	for j in range(len(kmer2)):
		if kmer1[i]==kmer2[j]:
			print('(',i,',',j,')')
			break
for i in range(len(kmer1)):
	for j in range(len(rev)):
		if kmer1[i]==rev[j]:
			print('(',i,',',j,')')
			break
#In:
#3
#AAACTCATC
#TTTCAAATC
#Out:
#(0, 4) 
#(0, 0) 
#(4, 2) 
#(6, 6) 