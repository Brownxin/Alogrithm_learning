import re

s=" 3+5 / 2"
print(s)
s = re.sub(r'\d+', ' \g<0> ', s)
# print(s)
# s.strip()
t=s.split()
print(t)


