f=lambda s,c=1:s[0]+str(c)+f(s[1:])if s and(len(s)<2or s[0]!=s[1])else f(s[1:],c+1)if s else''
print(f(input()))

