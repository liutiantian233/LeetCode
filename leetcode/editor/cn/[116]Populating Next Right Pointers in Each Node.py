# You are given a perfect binary tree where all leaves are on the same level, 
# and every parent has two children. The binary tree has the following definition: 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#  
# 
#  Populate each next pointer to point to its next right node. If there is no 
# next right node, the next pointer should be set to NULL. 
# 
#  Initially, all next pointers are set to NULL. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function 
# should populate each next pointer to point to its next right node, just like in 
# Figure B. The serialized output is in level order as connected by the next 
# pointers, with '#' signifying the end of each level.
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 2¹² - 1]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  
#  Follow-up: 
# 
#  
#  You may only use constant extra space. 
#  The recursive approach is fine. You may assume implicit stack space does not 
# count as extra space for this problem. 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 586 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root_node = root
        first_node = None
        next_node = None
        while root_node:
            if root_node.left:
                if first_node is None:
                    first_node = root_node.left
                if next_node is not None:
                    next_node.next = root_node.left
                next_node = root_node.left
            if root_node.right:
                if first_node is None:
                    first_node = root_node.right
                if next_node is not None:
                    next_node.next = root_node.right
                next_node = root_node.right
            root_node = root_node.next
            if root_node is None:
                root_node = first_node
                first_node = None
                next_node = None
        return root

# leetcode submit region end(Prohibit modification and deletion)


s = Solution()

n_7 = Node()
n_7.val = 7

n_6 = Node()
n_6.val = 6

n_5 = Node()
n_5.val = 5

n_4 = Node()
n_4.val = 4

n_3 = Node()
n_3.val = 3
n_3.left = n_6
n_3.right = n_7

n_2 = Node()
n_2.val = 2
n_2.left = n_4
n_2.right = n_5

n_1 = Node()
n_1.val = 1
n_1.left = n_2
n_1.right = n_3

print(s.connect(n_1).left.next.val)
