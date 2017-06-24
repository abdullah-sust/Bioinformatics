Text = 'AATCGGGTTCAATCGGGGT'
Pattern=['ATCG','GGGT']
ans=[]
for i in range(len(Pattern)):
	for j in range(len(Text)-len(Pattern[i])+1):
		if Pattern[i]==Text[j:j+len(Pattern[i])]:
			ans+=[j]
ans=sorted(ans)
s=""
for i in range(len(ans)):
	s+=" "+str(ans[i])
print(s)
#In:
#AATCGGGTTCAATCGGGGT
#ATCG
#GGGT
#Out:
# 1 4 11 15