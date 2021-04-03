# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#  
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#  
# Constraints:
#
#
# 	1 <= s.length, t.length <= 5 * 104
# 	s and t consist of lowercase English letters.
#
#
#  
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
                
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
        
        for k,v in d.items():
            if v != 0:
                return False
        
        return True
