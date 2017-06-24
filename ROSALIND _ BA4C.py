Spectrum = {'G':57,'A':71,'S':87,'P':97,
			 'V':99,'T':101,'C':103,'I':113,
			 'L':113,'N':114,'D':115,'K':128,
			 'Q':128,'E':129,'M':131,'H':137,
			 'F':147,'R':156,'Y':163,'W':186}
Peptide = str(input())
l = len(Peptide)
Peptide = Peptide + Peptide
arr = {}
arr[""]=0
i=0
k=1
while l!=k:
	if Peptide[i:i+k] not in arr:
		z=0
		s=Peptide[i:i+k]
		for m in range(len(s)):
			z+=Spectrum[s[m]]
		arr[s]=z
	else:
		k+=1
		i=-1
	i+=1
z=0
for i in range((int)(len(Peptide)/2)):
	z+=Spectrum[Peptide[i]]
arr[Peptide[0:(int)(len(Peptide)/2)]]=z
a=sorted(arr.values())
ans=""
for i in range(len(a)):
	ans+=" "+str(a[i])
print(ans)
#In:
#LEQN
#Out:
#0 113 114 128 129 227 242 242 257 355 356 370 371 484