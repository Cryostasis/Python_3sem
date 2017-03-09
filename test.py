fi = open('input.txt', 'r')
fo = open('output.txt', 'w')

(L, R, E) = map(int, fi.read().split())

N = (3 + 2 * R + 2 * E - L) * L - 1

ans = []
for i in range(0, N):
	ans.append(['.' * N])

def setCh(x, y, ch):
	ans[x][y] = ch if (ans[x][y] == '.') else 'x'

def boom(l, r, e, x, y):
	setCh(x, y, '*')
	for i in range(0, r):
		setCh(x, y + i, '-')
		setCh(x, y - i, '-')
		setCh(x + i, y, '|')
		setCh(x - i, y, '|')

	for i in range(0, r + e):
		setCh(x + i, y + i, '\\')
		setCh(x + i, y - i, '/')
		setCh(x - i, y + i, '/')
		setCh(x - i, y - i, '\\')
	boom(l - 1, r - 1, e, x + r + e, y)
	boom(l - 1, r - 1, e, x - r - e, y)
	boom(l - 1, r - 1, e, x, y + r + e)
	boom(l - 1, r - 1, e, x, y - r - e)

boom(L, R, E, int(N / 2) + 1, int(N / 2) + 1)

for i in range(0, N):
	print("".join(ans[i]))