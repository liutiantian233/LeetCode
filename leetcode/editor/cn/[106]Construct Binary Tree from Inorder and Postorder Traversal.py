# Given two integer arrays inorder and postorder where inorder is the inorder 
# traversal of a binary tree and postorder is the postorder traversal of the same 
# tree, construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 616 👎 0

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def find_root(in_order: List[int], post_order: List[int]):
            if post_order:
                node = TreeNode()
                root = post_order.pop(-1)
                index = in_order.index(root)
                in_order.remove(root)
                node.val = root

                left_in_order = in_order[:index]
                right_in_order = in_order[index:]
                left_post_order = post_order[:len(left_in_order)]
                right_post_order = post_order[len(left_in_order):]

                node.left = find_root(left_in_order, left_post_order)
                node.right = find_root(right_in_order, right_post_order)

                return node
            else:
                return None

        tree = find_root(inorder, postorder)
        return tree
# leetcode submit region end(Prohibit modification and deletion)


a = Solution()
t = a.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(t.right.right.left)

