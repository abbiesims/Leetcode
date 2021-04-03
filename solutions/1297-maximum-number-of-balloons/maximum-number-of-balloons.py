# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
#
# You can use each character in text at most once. Return the maximum number of instances that can be formed.
#
#  
# Example 1:
#
#
#
#
# Input: text = "nlaebolko"
# Output: 1
#
#
# Example 2:
#
#
#
#
# Input: text = "loonbalxballpoon"
# Output: 2
#
#
# Example 3:
#
#
# Input: text = "leetcode"
# Output: 0
#
#
#  
# Constraints:
#
#
# 	1 <= text.length <= 10^4
# 	text consists of lower case English letters only.
#


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for char in text:
            if char in d:
                d[char] += 1
        
        d["l"] //= 2
        d["o"] //= 2
        
        return min(d.values())
    
    
#         counter = {"b":0, "a":0, "l":0, "o":0, "n":0}
#         for char in text:
#             if char in counter:
#                 counter[char] += 1
#         counter["l"] //= 2
#         counter["o"] //= 2
#         return min(counter.values())    
