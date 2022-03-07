n = int(input())
ans = 0
for i in range(n):
	sure = 0
	x = input().split()
	for i in x:	
		sure += int(i)
	if sure > 1:
		ans += 1
print(ans)
