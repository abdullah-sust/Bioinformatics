kmer = ['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']
ans ={}
arr = [[0 for i in range(100)] for j in range (100)]
j=0
for i in range(len(kmer)):
	if kmer[i][0:len(kmer[i])-1] not in arr:
		arr[j]=kmer[i][0:len(kmer[i])-1]
		j+=1
		ans[kmer[i][0:len(kmer[i])-1]]=kmer[i][1:len(kmer[i])]
	else:
		ans[kmer[i][0:len(kmer[i])-1]]=ans[kmer[i][0:len(kmer[i])-1]]+','+kmer[i][1:len(kmer[i])]
#print(ans)
for key, val in ans.items():
	print (key, ' -> ', val)
#In:
#GAGG 
#CAGG 
#GGGG 
#GGGA 
#CAGG 
#AGGG 
#GGAG
#Out:
#GAG  ->  AGG
#GGG  ->  GGG,GGA
#AGG  ->  GGG
#GGA  ->  GAG
#CAG  ->  AGG,AGG