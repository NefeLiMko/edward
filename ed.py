import sys

filename = sys.argv[1]
f = open(filename,'r')
s = f.read()
res = ''
itr = enumerate(s)

for ind, ch in itr:
    if ind <len(s)-1 and ch == s[ind+1]:
        next(itr)
    else:
        res += ch
    
print(res)