#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    # def addBinary(self, a: str, b: str) -> str:
    #     """
    #     Accepted
    #     296/296 cases passed (34 ms)
    #     Your runtime beats 66.81 % of python3 submissions
    #     Your memory usage beats 19.87 % of python3 submissions (13.9 MB)
    #     """
    #     if len(a) < len(b):
    #         a, b = b, a

    #     # a is always larger
    #     b = '0' * (len(a) - len(b)) + b
    #     assert(len(a) == len(b))

    #     carry = False
    #     result = ""
    #     for i in range(len(a) -1, -1, -1):
    #         if a[i] == '1' and b[i] == '1':
    #             if carry:
    #                 result += '1'
    #             else:
    #                 result += '0'
    #             carry = True
    #         elif a[i] == '0' and b[i] == '0':
    #             if carry:
    #                 result += '1'
    #             else:
    #                 result += '0'
    #             carry = False
    #         else: # 1 and 0
    #             if carry:
    #                 result += '0'
    #                 carry = True
    #             else:
    #                 result += '1'
    #                 carry = False
    #     if carry:
    #         result += '1'

    #     return result[::-1]

    def addBinary(self, a: str, b: str) -> str:
        def helper(_a, _b, _carry=False):
            if not _a and _carry:
                return '1'
            
            if not _a:
                return ''
            a_val = ord(_a[-1]) - ord('0')
            b_val = ord(_b[-1]) - ord('0')

            val = a_val + b_val
            carry = False
            if val == 2:
                if _carry:
                    val = 1
                else:
                    val = 0
                carry = True
            elif val == 1:
                if _carry:
                    carry = True
                    val = 0
                else:
                    val = 1
            else:
                if _carry:
                    val = 1
                else:
                    val = 0

            return helper(_a[:-1], _b[:-1], carry) + str(val)

        if len(a) < len(b):
            a, b = b, a

        # a is always larger
        b = '0' * (len(a) - len(b)) + b
        return helper(a, b)








# @lc code=end

