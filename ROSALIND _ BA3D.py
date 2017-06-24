k = int(input())
Text = str(input())
ans = {}
kmer =[[0 for i in range(100)]for i in range(100)]
j=0
for i in range(len(Text)-k+1):
	if Text[i:i+k-1] not in kmer:
		kmer[j]= Text[i:i+k-1]
		j+=1
		ans[Text[i:i+k-1]]=Text[i+1:i+k]
	else:
		ans[Text[i:i+k-1]]=ans[Text[i:i+k-1]]+','+ Text[i+1:i+k]
for key,val in ans.items():
	print(key,' -> ',val)
#In:
#4
#AAGATTCTCTAC
#Out:
#AAG ‐> AGA 
#AGA ‐> GAT 
#ATT ‐> TTC 
#CTA ‐> TAC 
#CTC ‐> TCT 
#GAT ‐> ATT 
#TCT ‐> CTA,CTC 
#TTC ‐> TCT
