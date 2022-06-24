# Pascal's Triangle

Given an integer `numRows`, return the first numRows of **Pascal's triangle.** <br/>
In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

<br/>

**Example 1:**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2:**

```
Input: numRows = 1
Output: [[1]]
```

**Constraints:**

* `1 <= numRows <= 30`

<br/>

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1],[1,1]]
        if numRows == 1:
            return dp[:1]
        elif numRows == 2:
            return dp
        else:
            for _ in range(numRows-2):
                temp = [1]
                for i in range(len(dp[-1])-1):
                    temp.append(dp[-1][i] + dp[-1][i+1])
                dp.append(temp+[1])
            return dp
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range (numRows-1):
            temp=[0]+res[-1]+[0]
            row =[] 
            for j in range (len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)
        return res
"""
```