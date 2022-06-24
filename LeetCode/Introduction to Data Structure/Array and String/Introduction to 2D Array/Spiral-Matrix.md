# Spiral Matrix

Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.

<br/> 

**Example 1:**
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2:**
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

<br/> 

[참고](https://velog.io/@jiselectric/Leetcode-Spiral-Matrix)

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            result += matrix.pop(0) # 상

            if matrix and matrix[0]: # 우
                for row in matrix:
                    result.append(row.pop())

            if matrix: # 하
                result += matrix.pop()[::-1]

            if matrix and matrix[0]: # 좌
                for row in matrix[::-1]:
                    result.append(row.pop(0))

        return result

"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
"""
```