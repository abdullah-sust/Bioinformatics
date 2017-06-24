dna1 = str(input())
dna2 = str(input())
dis=0
for i in range(len(dna1)):
    if dna1[i]!=dna2[i]:
        dis+=1
print(dis)
#In:
#GGGCCGTTGGT
#GGACCGTTGAC
#Out:
#3