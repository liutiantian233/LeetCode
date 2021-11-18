# Given an m x n matrix board containing 'X' and 'O', capture all regions that 
# are 4-directionally surrounded by 'X'. 
# 
#  A region is captured by flipping all 'O's into 'X's in that surrounded 
# region. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X",
# "O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X",
# "X"]]
# Explanation: Surrounded regions should not be on the border, which means that 
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not 
# on the border and it is not connected to an 'O' on the border will be flipped to 
# 'X'. Two cells are connected if they are adjacent cells connected horizontally 
# or vertically.
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["X"]]
# Output: [["X"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] is 'X' or 'O'. 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 655 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(x, y):
            board[x][y] = "Z"
            for i, j in ([x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]):
                if 0 <= i < rows and 0 <= j < cols and board[i][j] == "O":
                    dfs(i, j)

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
                    if board[row][col] == "O":
                        dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if row != 0 and col != 0 and row != len(board) - 1 and col != len(board[0]) - 1:
                    if board[row][col] == "O":
                        board[row][col] = "X"
                if board[row][col] == "Z":
                    board[row][col] = "O"
# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
board_ = [["O","O","O"],["O","O","O"],["O","O","O"]]
print(s.solve(board_))
