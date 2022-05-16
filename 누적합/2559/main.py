n, k = map(int, input().split())
temp = list(map(int, input().split()))

ans = sum(temp[:k]) # 최대값(=정답) 변수
num = ans # 모든 구간 합을 체크할 변수
for i in range(n-k):
    num += (temp[i+k] - temp[i]) # num : i+1번째에서 시작하는 구간합 값
    if num > ans:
        ans = num
print(ans)