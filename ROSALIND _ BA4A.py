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

Pattern = str(input())
r = len(Pattern)
i=0
acid=""
while i<r:
	if Peptide[Pattern[i:i+3]]=='*':
		break;
	else:
		acid+=Peptide[Pattern[i:i+3]]
	i+=3
print(acid)
#In:
#AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
#Out:
#MAMAPRTEINSTRING