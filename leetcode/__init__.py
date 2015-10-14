from filecmp import cmp
from functools import cmp_to_key

a=['1','3']
def compare(self,a):
    b='2'

    if a>b:
        return 1
    else: return -1
b=sorted(a,key=cmp_to_key(compare))
print(a,b)