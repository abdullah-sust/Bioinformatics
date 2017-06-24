Patterns=['ATAGA','ATC','GAT']
kmer=[]
h=[]
t=[]
m=0
n=0
edgeH={"":0}
edgeT={}
ans=[]
for i in range(len(Patterns)):
	for j in range(len(Patterns[i])):
		if Patterns[i][0:j+1] not in kmer:
			kmer+=[Patterns[i][0:j+1]]
			ans+=[Patterns[i][j]]
			if len(Patterns[i][0:j+1])==1:
				m=0
				h+=[m]
			else:
				s=Patterns[i][0:j]
				for x in range(len(kmer)):
					if s==kmer[x]:
						h+=[t[x]]

			n+=1
			t+=[n]


for i in range(len(ans)):
    print(h[i],"->",t[i],":",ans[i])

#In:
#ATAGA
#ATC
#GAT

#Out:
#0 -> 1 : A
#1 -> 2 : T
#2 -> 3 : A
#3 -> 4 : G
#4 -> 5 : A
#2 -> 6 : C
#0 -> 7 : G
#7 -> 8 : A
#8 -> 9 : T
