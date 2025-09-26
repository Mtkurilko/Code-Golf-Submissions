f=lambda s,c=1:s and(s[0]+str(c)+f(s[1:]) if not s[1:]or s[0]!=s[1] else f(s[1:],c+1))or''
print(f(input()))

