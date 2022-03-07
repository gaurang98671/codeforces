s = [int(x) for x in input().split("+")]

s.sort()
for i in range(len(s)):
	s[i] = str(s[i])
print("+".join(s))
