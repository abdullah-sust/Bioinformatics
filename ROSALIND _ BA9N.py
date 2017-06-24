Text='AATCGGGTTCAATCGGGGT'
Pattern=['ATCG','GGGT']
ans=[]
for j in range(len(Pattern)):
	for i in range(len(Text)-len(Pattern[j])+1):
		p=Pattern[j]
		s=Text[i:i+len(Pattern[j])]
		m=0
		for x in range(len(Pattern[j])):
			if p[x]!=s[x]:
				m+=1
		if m==0:
			ans+=[i]
for i in range(len(ans)-1):
	j=i+1
	while j<len(ans):
		if ans[i]>ans[j]:
			t=ans[i]
			ans[i]=ans[j]
			ans[j]=t
		j+=1
a=""
for i in range(len(ans)):
	a+=" "+str(ans[i])
print(a)