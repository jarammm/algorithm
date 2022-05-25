n, m = map(int, input().split())
nums = list(map(int, input().split()))
mlist = [0 for i in range(m)]
cumsum = 0
mlist[0] = 1

for i in range(n):
    cumsum += nums[i]
    mlist[cumsum%m] += 1

ans = 0

# 구간 [l, r]의 합을 m으로 나눈 나머지가 0이라는 것은 [0, l - 1]과 [0, r]의 cumsum%m의 값이 같다는 것과 동일
for i in mlist:
    ans += i*(i-1)//2

print(ans)