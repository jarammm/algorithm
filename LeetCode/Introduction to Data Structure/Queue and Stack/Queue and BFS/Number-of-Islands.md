Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.
<br/>
An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
<br/>
<br/>


**Example 1:**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2:**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

<br/>

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m, n <= 300`
* `grid[i][j]` is `'0'` or `'1'`.

<br/>

Answer Code:

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,x,y):
            grid[x][y] = "0" # 섬을 확인했다는 의미로, 섬을 바다로 변경(섬 방문 체크 용도)
            if x+1 < len(grid) and grid[x+1][y] == "1": # 오른쪽 칸 존재 + 섬일 때
                dfs(x+1,y) # 오른쪽 섬으로 이동
            if x-1 >= 0  and grid[x-1][y] == "1": # 왼쪽 칸 존재 + 섬일 때
                dfs(x-1,y) # 왼쪽 섬으로 이동
            if y+1 < len(grid[0]) and grid[x][y+1] == "1": # 위쪽 칸 존재 + 섬일 때
                dfs(x,y+1) # 위쪽 섬으로 이동
            if y-1 >= 0 and grid[x][y-1] == "1": # 아래쪽 칸 존재 + 섬일 때
                dfs(x,y-1) # 아래쪽 섬으로 이동

        islands = 0 # 섬 개수 세는 변수
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    islands += 1
                    dfs(grid,x,y) # 하나의 island의 면적 체크
        return islands
```