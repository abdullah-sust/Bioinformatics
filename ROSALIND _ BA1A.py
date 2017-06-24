def PatternCount(Text,Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Pattern==Text[i:i+len(Pattern)]:
            count=count+1
    return count

Text = str(input())
Pattern = str(input())
print( (PatternCount(Text,Pattern)))
#INPUT:
#GCGCG
#GCG
#OUTPUT:
#2