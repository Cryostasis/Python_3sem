import re

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')

S = fi.read()
print(S)
#leftR = r"^[\w\*\+]*(?=sin())"
#sinR = r"(?<=\()[\w\*\+]*(?=\))"
#rightR = r"(?<=[\)])[\w\*\+]*$"

findxR = r"[1-9x\*]*"

sinR = r"[0-9x\*]*sin\([\w\*\+]*\)"
leftR = r"^[\w\*\+]*?(?=[0-9x\*]*sin\([\w\*\+]*\))"
rightR = r"^[\w\*\+]*?(?=[0-9x\*]*\)[\w\*\+]*\(nis)"
insR = r"(?<=\()[\w\*\+]*(?=\))"


left = list(re.search(leftR, S).group(0)[::-1])
sin = list(re.search(sinR, S).group(0))
right = list(re.search(rightR, S[::-1]).group(0))
ins = list(re.search(sinR, S).group(0))

print(left)
print(sin)
print(right)

flg_out_x = 0
flg_out_0 = 0
