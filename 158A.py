n, k = [int(x) for x in input().split(' ')]
arr = [int(x) for x in input().split(' ')]

rnk = arr[k-1]

ans = 0

for i in arr:
	if i > 0 and i >= rnk:
		ans += 1
print(ans)