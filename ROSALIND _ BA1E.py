Genome = str(input())
k= int(input())
L= int(input())
t= int(input())
#print (k," ",L," ",t)

ans={}
for i in range(len(Genome)-L+1):
    s=Genome[i:i+L]
    temp={}
    for j in range(len(s)-k+1):
        if s[j:j+k] not in temp:
            temp[s[j:j+k]]=1
        else:
            temp[s[j:j+k]]=temp[s[j:j+k]]+1
        
    for key,val in temp.items():
        if(val>=t and key not in ans):
            ans[key]=val
            #print(key)
for key,val in ans.items():
    print(key)
#Input:
#CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC
#5 75 4
#Output:
#CGACA GAAGA AATGT