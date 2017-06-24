from itertools import product
Spectrum = [57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]
inp = [0,113,128,186,241,299,314,427]
mass = []
for i in range(len(inp)):
	if inp[i] in Spectrum:
		mass+=[str(inp[i])]
print(mass)
#ans = [''.join(i for i in product(mass,repeat=len(alpha)))]
#print(ans)