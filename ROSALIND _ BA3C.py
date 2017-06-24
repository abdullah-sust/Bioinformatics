Pattern = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']
#['AAGCT','ACCGA','CCGAA','CGAAG','GAAGC']
temp = [0 for i in range(len(Pattern))]
arr = {}
for i in range(len(Pattern)):
	arr[Pattern[i]]=0
l = len(Pattern[0])+len(Pattern)-1
i=1
Text = Pattern[0]
while len(Text)!=l:
	h = Text[0:len(Pattern[0])-1]
	t = Text[len(Text)-len(Pattern[0])+1]
	if t==Pattern[i][0:len(Pattern[0])-1] and arr[Pattern[i]]==0:
		arr[Pattern[i]]=1
		Text+=Pattern[i][len(Pattern[i])-1]
		i=0
	if h==Pattern[i][1:len(Pattern[0])] and arr[Pattern[i]]==0:
		arr[Pattern[i]]=1
		Text=Pattern[i][0]+Text
		i=0
	i+=1
l=len(Pattern[0])
ans = {}
for i in range(len(Text)-l):
	print(Text[i:i+l],'->',Text[i+1:i+l+1])
#In:
#ATGCG 
#GCATG 
#CATGC 
#AGGCA 
#GGCAT
#Out:
#AGGCA -> GGCAT
#GGCAT -> GCATG
#GCATG -> CATGC
#CATGC -> ATGCG