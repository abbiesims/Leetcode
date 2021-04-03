# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
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
# 	You may assume that both strings contain only lowercase letters.
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
            
