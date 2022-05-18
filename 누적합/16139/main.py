import sys
input = sys.stdin.readline

s = input().rstrip()
letters = [[0]*26]
for i in range(1,len(s)+1):
    letters.append(letters[-1][:])
    letters[i][ord(s[i-1])-97] += 1

for _ in range(int(input())):
    a,l,r = list(input().split())
    a,l,r = ord(a), int(l), int(r)
    print(letters[r+1][a-97]-letters[l][a-97])