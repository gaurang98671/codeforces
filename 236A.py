name = input()
d = {}
ans = 0
for i in name:
	if i not in d:
		d[i] = 1
		ans += 1
if ans % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")