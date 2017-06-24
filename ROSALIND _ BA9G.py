Text='AACGATAGCGGTAGA$'
ans=[]
ans=[len(Text)-1]

l=len(Text)-1
while l>-1:
	if Text[l]=='A':
		ans+=[l]
	l-=1
l=len(Text)-1
while l>-1:
	if Text[l]=='C':
		ans+=[l]
	l-=1
l=len(Text)-1
while l>-1:
	if Text[l]=='G':
		ans+=[l]
	l-=1
l=len(Text)-1
while l>-1:
	if Text[l]=='T':
		ans+=[l]
	l-=1
print(ans)
