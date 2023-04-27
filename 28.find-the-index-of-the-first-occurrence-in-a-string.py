#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     """
    #     Accepted
    #     79/79 cases passed (28 ms)
    #     Your runtime beats 81.69 % of python3 submissions
    #     Your memory usage beats 94.25 % of python3 submissions (13.8 MB)
    #     """
    #     for i in range(len(haystack)):
    #         if haystack[i:len(needle)+i] == needle:
    #             return i

    #     return -1
    def hash_func(self, str):
        result = 0
        for c in str:
            result = result * 31 + ord(c)
        return result


    def hash_func2(self, str):
        result = 0
        str_length = len(str)
        for i in range(str_length):
            result += ord(str[i]) * 31 ** (str_length - 1 - i)
        return result


    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        needle_hash = self.hash_func2(needle)

        substr_hash = self.hash_func2(haystack[0:needle_len])
        for i in range(haystack_len - needle_len + 1):
            substr = haystack[i:i+needle_len]
            if substr_hash == needle_hash:
                if substr == needle:
                    return i

            if i < haystack_len - needle_len:
                # substr_hash = substr_hash * 31 - ord(haystack[i]) * 31 ** needle_len + ord(haystack[i+needle_len])
                substr_hash = 31 * (substr_hash - ord(haystack[i]) * 31 ** (needle_len - 1)) + ord(haystack[i+needle_len])

        return -1



        

# @lc code=end
