from re import *
text="fat cat run very fast to catch the mouse"
pattern="at"
matcher=finditer(pattern,text)
#return - start() 1         5
#group()          at        at
for m in matcher:
    print(m.start(),m.group())