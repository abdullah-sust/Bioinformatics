Genome = str(input())
count=0;
arr=[0]
min=100000000
for i in range(len(Genome)):
	if Genome[i]=='G':
		count+=1
	elif Genome[i]=='C':
		count-=1
	if(count<min):
		min=count
	arr+=[count]
ans =""
for i in range(len(Genome)):
	if arr[i]==min:
		ans+=" "+str(i)
print (ans)
#In:
#CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG
#Out:
#53 97
