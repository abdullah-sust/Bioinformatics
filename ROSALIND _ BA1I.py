Text=str(input())
k=int(input())
d=int(input())

def hamDis(s1,s2):
	m=0
	for l in range(len(s1)):
		if s1[l]!=s2[l]:
			m+=1
	if m<=d:
		return 1
	return 0

ans={}

def occur(s):
	n=0
	for j in range(len(Text)-k+1):
		t=hamDis(s,Text[j:j+k])
		if t==1:
			n+=1
	return n

for i in range(len(Text)-k+1):
	ans[Text[i:i+k]]=occur(Text[i:i+k])

max=-1000000
for key,val in ans.items():
    if(val>max):
        max=val
a=""
for key,val in ans.items():
    if(val==max):
        a+=str(key)+" "
    
print(a)

#Input:
#ACGTTGCATGTCGCATGATGCATGAGAGCT
#4 1
#Output:
#GATG ATGC ATGT