# A path in a binary tree is a sequence of nodes where each pair of adjacent 
# nodes in the sequence has an edge connecting them. A node can only appear in the 
# sequence at most once. Note that the path does not need to pass through the root. 
# 
# 
#  The path sum of a path is the sum of the node's values in the path. 
# 
#  Given the root of a binary tree, return the maximum path sum of any non-
# empty path. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 
# = 42.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 3 * 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 1280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import Optional
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None
        self.queue = []

    def add(self, element):
        node = TreeNode(element)
        if self.root is None:
            self.root = node
            self.queue.append(self.root)
        else:
            tree_node = self.queue[0]
            if tree_node.left is None:
                tree_node.left = node
                self.queue.append(tree_node.left)
            else:
                tree_node.right = node
                self.queue.append(tree_node.right)
                self.queue.pop(0)


class Solution:
    def __init__(self):
        self.max_path = -sys.maxsize

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def return_path(node: Optional[TreeNode]):
            if not node:
                return -sys.maxsize
            left_node = return_path(node.left)
            right_node = return_path(node.right)
            self.max_path = max(self.max_path, node.val + left_node + right_node, left_node, right_node)
            return max(node.val, node.val + left_node, node.val + right_node)
        max_path = return_path(root)
        return max(self.max_path, max_path)

# leetcode submit region end(Prohibit modification and deletion)


s = Solution()
n_5 = TreeNode()
n_5.val = 15
n_4 = TreeNode()
n_4.val = 7
n_3 = TreeNode()
n_3.val = 9
n_2 = TreeNode()
n_2.val = 20
n_2.left = n_5
n_2.right = n_4
n_1 = TreeNode()
n_1.val = -10
n_1.left = n_3
n_1.right = n_2
print(s.maxPathSum(n_1))
