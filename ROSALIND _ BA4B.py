Peptide =  {'AUG':'M','AUA':'I','AUC':'I','AUU':'I',
			'AGG':'R','AGA':'R','AGC':'S','AGU':'S',
			'ACG':'T','ACA':'T','ACC':'T','ACU':'T',
			'AAG':'K','AAA':'K','AAC':'N','AAU':'N',
			'UUG':'L','UUA':'L','UUC':'F','UUU':'F',
			'UGG':'W','UGA':'*','UGC':'C','UGU':'C',
			'UCG':'S','UCA':'S','UCC':'S','UCU':'S',
			'UAG':'*','UAA':'*','UAC':'Y','UAU':'Y',
			'GUG':'V','GUA':'V','GUC':'V','GUU':'V',
			'GGG':'G','GGA':'G','GGC':'G','GGU':'G',
			'GCG':'A','GCA':'A','GCC':'A','GCU':'A',
			'GAG':'E','GAA':'E','GAC':'D','GAU':'D',
			'CUG':'L','CUA':'L','CUC':'L','CUU':'L',
			'CGG':'R','CGA':'R','CGC':'R','CGU':'R',
			'CCG':'P','CCA':'P','CCC':'P','CCU':'P',
			'CAG':'Q','CAA':'Q','CAC':'H','CAU':'H'}
P = str(input())
acid = str(input())
l = len(acid)*3
def func(st):
	t=0
	i=0
	k=0
	while i<l:
		if Peptide[st[i:i+3]]==acid[k]:
			t=1
		else:
			t=0
			break
		i+=3
		k+=1
	if t==1:
		return True
	else:
		return False

def rna(str):
	ans=""
	for i in range(len(str)):
		if str[i]=='U':
			ans+='T'
		else:
			ans+=str[i]
	return ans 

Pattern=""
for i in range(len(P)):
    if P[i]=='T':
        Pattern+='U'
    else:
        Pattern+=P[i]
#print(Pattern)
for i in range(len(Pattern)-l+1):
	s=func(Pattern[i:i+l])
	if s==True:
		print(rna(Pattern[i:i+l]))
	else:
		t=len(P[i:i+l])-1
		st=P[i:i+l]
		pp=""
		while t>-1:
			#print(st[t])
			if st[t]=='A':
				pp+='U'
			if st[t]=='T':
				pp+='A'
			if st[t]=='G':
				pp+='C'
			if st[t]=='C':
				pp+='G'
			t-=1
		#print('---------')

		#print(P[i:i+l],"->",pp)
		if func(pp)==True:
#			print('-')
			print(P[i:i+l])

#In:
#ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
#MA
#Out:
#ATGGCC
#GGCCAT
#ATGGCC
