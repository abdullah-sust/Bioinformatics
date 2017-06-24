k = int(input())
Text = str(input())
for i in range(len(Text)-k+1):
	print(Text[i:i+k])
#In:
#5
#CAATCCAAC
#Out:
#AATCC 
#ATCCA 
#CAATC 
#CCAAC 
#TCCAA