Pattern = str(input())
Genome = str(input())

pos=""
for i in range(len(Genome)-len(Pattern)+1):
	if Genome[i:i+len(Pattern)]==Pattern:
		pos+=" "+str(i)
print(pos)
#Input:
#ATAT
#GATATATGCATATACTT
#Output
# 1 3 9