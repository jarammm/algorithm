# Diagonal Traverse

Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.

<br/>

**Example 1:**

```
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
```

**Example 2:**

```
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
```

**Constraints:**

* `m == mat.length`
* `n == mat[i].length`
* `1 <= m, n <= 104`
* `1 <= m * n <= 104`
* `-105 <= mat[i][j] <= 105`

<br/>

```python
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        dd = collections.defaultdict(list)
        if not mat: return result
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                dd[i+j+1].append(mat[i][j])
        for k in sorted(dd.keys()):
            if k%2==1: dd[k].reverse()
            result += dd[k]
        return result
```