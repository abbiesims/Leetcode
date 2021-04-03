# Given an integer n, add a dot (".") as the thousands separator and return it in string format.
#
#  
# Example 1:
#
#
# Input: n = 987
# Output: "987"
#
#
# Example 2:
#
#
# Input: n = 1234
# Output: "1.234"
#
#
# Example 3:
#
#
# Input: n = 123456789
# Output: "123.456.789"
#
#
# Example 4:
#
#
# Input: n = 0
# Output: "0"
#
#
#  
# Constraints:
#
#
# 	0 <= n < 2^31
#
#


class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) < 4:
            return str(n)
        s = str(n)
        thousands = []
        remainder = len(s) % 3
        thousands.append(s[:remainder])
        newS = s[remainder:]
        for i in range(0, len(newS)-2, 3):
            thousands.append(newS[i:i+3])
        
        
        ans = ".".join(thousands)
        if ans[0] == '.':
            return ans[1:]
        return ans
