n = int(input())
arr = [int(x) for x in input().split(' ')]
min_ele = arr[0]
max_ele = arr[0]
ans = 0
for i in range(1, len(arr)):
	if arr[i] < min_ele or arr[i] > max_ele:
		ans += 1
	min_ele = min(min_ele, arr[i])
	max_ele = max(max_ele, arr[i])
print(ans)
	