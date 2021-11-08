# In an alien language, surprisingly, they also use English lowercase letters,
# but possibly in a different order. The order of the alphabet is some permutation 
# of lowercase letters. 
# 
#  Given a sequence of words written in the alien language, and the order of 
# the alphabet, return true if and only if the given words are sorted 
# lexicographically in this alien language. 
# 
#  
#  Example 1: 
# 
#  
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is 
# sorted.
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1]
# , hence the sequence is unsorted.
#  
# 
#  Example 3: 
# 
#  
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is 
# shorter (in size.) According to lexicographical rules "apple" > "app", because 
# 'l' > '∅', where '∅' is defined as the blank character which is less than any 
# other character (More info).
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= words.length <= 100 
#  1 <= words[i].length <= 20 
#  order.length == 26 
#  All characters in words[i] and order are English lowercase letters. 
#  
#  Related Topics 数组 哈希表 字符串 👍 96 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for index_i, i in enumerate(words[:-1]):
            front = i
            after = words[index_i + 1]
            if len(after) < len(front):
                after += (len(front) - len(after)) * " "
            elif len(after) > len(front):
                front += (len(after) - len(front)) * " "
            for index_j, j in enumerate(front):
                if order.find(j) < order.find(after[index_j]):
                    break
                elif order.find(j) == order.find(after[index_j]):
                    continue
                else:
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
