# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes contains a 
# single digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the 
# number 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have 
# leading zeros. 
#  
#  Related Topics 递归 链表 数学 👍 7072 👎 0

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def every_next(x: ListNode, y: ListNode, degree, ret_node: ListNode):
            if x.val or y.val or degree:
                ret_node.val = (x.val + y.val + degree) % 10
                degree = (x.val + y.val + degree) // 10
            if x.next and y.next:
                ret_node.next = ListNode(0)
                every_next(x.next, y.next, degree, ret_node.next)
            elif not x.next and y.next:
                ret_node.next = ListNode(0)
                every_next(ListNode(0), y.next, degree, ret_node.next)
            elif not y.next and x.next:
                ret_node.next = ListNode(0)
                every_next(x.next, ListNode(0), degree, ret_node.next)
            elif degree:
                ret_node.next = ListNode(0)
                every_next(ListNode(0), ListNode(0), degree, ret_node.next)

        ret = ListNode(0)
        every_next(l1, l2, 0, ret)
        return ret
# leetcode submit region end(Prohibit modification and deletion)


n3 = ListNode(3)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)

n6 = ListNode(4)
n5 = ListNode(6, n6)
n4 = ListNode(5)

s = Solution()
s.addTwoNumbers(n1, n4)
