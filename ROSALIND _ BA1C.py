Pettern = str(input())

revCom=""
i=len(Pettern)-1
while i>-1:
	if(Pettern[i]=='A'):
		revCom+='T'
	if(Pettern[i]=='T'):
		revCom+='A'
	if(Pettern[i]=='G'):
		revCom+='C'
	if(Pettern[i]=='C'):
		revCom+='G'
	i-=1
print (revCom)
#INPUT:
#AAAACCCGGT
#OUTPUT:
#ACCGGGTTTT