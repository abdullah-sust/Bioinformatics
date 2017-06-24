Spectrum = [0,137,186,323]
con = []
j=1
while j<len(Spectrum):
	for i in range(len(Spectrum)):
		if (Spectrum[j]-Spectrum[i])>0:
			con+=[(Spectrum[j]-Spectrum[i])]
	j+=1
#print(con)
ans = {}
for i in range(len(con)):
	if str(con[i]) not in ans:
		ans[str(con[i])]=1
	else:
		ans[str(con[i])]+=1
mx=max(ans.values())
out=""
while mx>0:
	for key,val in ans.items():
		if val==mx:
			for j in range(mx):
				out+=" "+key
	mx-=1
print(out)
#In:
#0 137 186 323
#Out:
#137 137 186 186 323 49 
