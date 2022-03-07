n = int(input())
stones = input()
ans = 0
for i in range(1, len(stones)):
	if stones[i] == stones[i - 1]:
		ans += 1
print(ans)