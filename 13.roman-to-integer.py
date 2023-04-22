#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def is_subtraction(self, index, s):
        digit = s[index]
        if digit == 'I':
            return self._one(index, s)
        elif digit == 'X':
            return self._ten(index, s)
        elif digit == 'C':
            return self._hundred(index, s)

        return False
    
    def _one(self, index, s):
        if index == len(s) - 1:
            return False

        if s[index + 1] == 'V' or s[index + 1] == 'X':
            return True
        return False
    
    def _ten(self, index, s):
        if index == len(s) - 1:
            return False

        if s[index + 1] == 'L' or s[index + 1] == 'C':
            return True
        return False

    def _hundred(self, index, s):
        if index == len(s) - 1:
            return False

        if s[index + 1] == 'D' or s[index + 1] == 'M':
            return True
        return False

    def romanToInt(self, s: str) -> int:
        """
        Accepted
        11510/11510 cases passed (68 ms)
        Your runtime beats 40.88 % of python3 submissions
        Your memory usage beats 45.39 % of python3 submissions (13.9 MB)
        """
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s)):
            if self.is_subtraction(i, s):
                result -= d[s[i]]
            else:
                result += d[s[i]]

        return result


# @lc code=end

