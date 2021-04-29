# Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#  
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
#  
# Constraints:
#
#
# 	1 <= ransomNote.length, magazine.length <= 105
# 	ransomNote and magazine consist of lowercase English letters.
#
#


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for char in magazine:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
            
        for c in ransomNote:
            if c not in d:
                return False
            else:
                d[c] -= 1
        
        for k,v in d.items():
            if v < 0:
                return False
            
        return True
            
