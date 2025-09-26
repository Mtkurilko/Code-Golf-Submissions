s=input();o='';i=0
while i<len(s):
    r=s[i:];c=len(r)-len(r.lstrip(s[i]));o+=s[i]+str(c);i+=c
print(o)