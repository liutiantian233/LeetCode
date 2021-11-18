# Given an m x n 2D binary grid grid which represents a map of '1's (land) and 
# '0's (water), return the number of islands. 
# 
#  An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] is '0' or '1'. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1405 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols, ret = len(grid), len(grid[0]), 0

        def dfs(x, y):
            grid[x][y] = "0"
            for i, j in ([x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]):
                if 0 <= i < rows and 0 <= j < cols and grid[i][j] == "1":
                    dfs(i, j)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    ret += 1

        return ret
# leetcode submit region end(Prohibit modification and deletion)
