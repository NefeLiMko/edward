import sys
import re

filename = sys.argv[1]
f = open(filename,'r')
s = f.read()
s = re.sub(r"\n","",s)
s = re.sub(r"(.)\1","",s)
print(s)
