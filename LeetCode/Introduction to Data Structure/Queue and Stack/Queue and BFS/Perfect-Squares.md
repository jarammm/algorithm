Given an integer `n`, return the least number of perfect square numbers that sum to `n`.<br/>

A **perfect square** is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, `1`, `4`, `9`, and 16 are perfect squares while `3` and `11` are not.<br/><br/>

**Example 1:**

```
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

**Constraints:**

* `1 <= n <= 10^4`

<br/>

* [Code 참고](https://www.youtube.com/watch?v=HLZLwjzIVGo)

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        
        for target in range(1, n+1):
            for square_root in range(1, target+1):
                square = square_root ** 2
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target - square])
        return dp[n], dp
    
    # O(n*n^1/2)
```

* 디버깅용 코드:

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n+1)
        dp[0] = 0
        
        for target in range(1, n+1):
            for square_root in range(1, target+1):
                square = square_root ** 2
                if target - square < 0:
                    break
                print("target:", target, "/ square_root:", square_root) #debugging
                print("dp[target]:", dp[target], "/ 1+dp[target - square]:", 1+dp[target - square]) #debugging
                dp[target] = min(dp[target], 1+dp[target - square])
                print("dp:", dp, "\n") #debugging
        return dp[n], dp
    
    # O(n*n^1/2)
```

* 디버깅 결과:

```
case = Solution()
case.numSquares(13)

========result========
target: 1 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 1
dp: [0, 1, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 2 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 2
dp: [0, 1, 2, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 3 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 4 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 4, 13, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 4 / square_root: 2
dp[target]: 4 / 1+dp[target - square]: 1
dp: [0, 1, 2, 3, 1, 13, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 5 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 5 / square_root: 2
dp[target]: 2 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 13, 13, 13, 13, 13, 13, 13, 13] 

target: 6 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13] 

target: 6 / square_root: 2
dp[target]: 3 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13] 

target: 7 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 13, 13, 13, 13, 13, 13] 

target: 7 / square_root: 2
dp[target]: 4 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 13, 13, 13, 13, 13, 13] 

target: 8 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 5
dp: [0, 1, 2, 3, 1, 2, 3, 4, 5, 13, 13, 13, 13, 13] 

target: 8 / square_root: 2
dp[target]: 5 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 13, 13, 13, 13, 13] 

target: 9 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 13, 13, 13, 13] 

target: 9 / square_root: 2
dp[target]: 3 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 13, 13, 13, 13] 

target: 9 / square_root: 3
dp[target]: 3 / 1+dp[target - square]: 1
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 13, 13, 13, 13] 

target: 10 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 13, 13, 13] 

target: 10 / square_root: 2
dp[target]: 2 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 13, 13, 13] 

target: 10 / square_root: 3
dp[target]: 2 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 13, 13, 13] 

target: 11 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 13, 13] 

target: 11 / square_root: 2
dp[target]: 3 / 1+dp[target - square]: 5
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 13, 13] 

target: 11 / square_root: 3
dp[target]: 3 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 13, 13] 

target: 12 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 4, 13] 

target: 12 / square_root: 2
dp[target]: 4 / 1+dp[target - square]: 3
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 13] 

target: 12 / square_root: 3
dp[target]: 3 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 13] 

target: 13 / square_root: 1
dp[target]: 13 / 1+dp[target - square]: 4
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 4] 

target: 13 / square_root: 2
dp[target]: 4 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2] 

target: 13 / square_root: 3
dp[target]: 2 / 1+dp[target - square]: 2
dp: [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2] 

(2, [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2]) # output

```
