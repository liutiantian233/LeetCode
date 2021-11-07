# Given an integer x, return true if x is palindrome integer. 
# 
#  An integer is a palindrome when it reads the same backward as forward. For 
# example, 121 is palindrome while 123 is not. 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  Example 4: 
# 
#  
# Input: x = -101
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string? 
# Related Topics 数学 👍 1674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        str_int = str_int[::-1]
        if str_int == str(x):
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
