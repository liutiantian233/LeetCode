# Given an m x n grid of characters board and a string word, return true if 
# word exists in the grid. 
# 
#  The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same letter 
# cell may not be used more than once. 
# 
#  
#  Example 1: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCCED"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "SEE"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCB"
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == board.length 
#  n = board[i].length 
#  1 <= m, n <= 6 
#  1 <= word.length <= 15 
#  board and word consists of only lowercase and uppercase English letters. 
#  
# 
#  
#  Follow up: Could you use search pruning to make your solution faster with a 
# larger board? 
#  Related Topics 数组 回溯 矩阵 👍 1083 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(x, y, index):
            if word[index] != board[x][y]:
                return False
            if index == len(word) - 1:
                return True
            board[x][y] = "#"
            for i, j in ([x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]):
                if 0 <= i < rows and 0 <= j < cols and dfs(i, j, index + 1):
                    return True
            board[x][y] = word[index]

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
