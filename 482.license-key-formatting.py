#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        formatted_s = ''
        for c in s:
            if c != '-':
                formatted_s += c.upper()

        first_group_len = len(formatted_s) % k
        result = []
        if first_group_len != 0:
            result.append(formatted_s[:first_group_len])
        i = first_group_len
        while i < len(formatted_s):
            result.append(formatted_s[i: i + k])
            i += k
        return '-'.join(result)

# @lc code=end
Solution().licenseKeyFormatting("5F3Z-2e-9-w",4)
