#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Accepted
        93/93 cases passed (35 ms)
        Your runtime beats 46.02 % of python3 submissions
        Your memory usage beats 56.93 % of python3 submissions (13.9 MB)
        """
        open_brackets = {'(', '[', '{'}
        close_brackets = {')', ']', '}'}
        corresponding_brackets = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        latest_open_bracket = []

        for i in s:
            if i in close_brackets:
                if not latest_open_bracket:
                    return False
                if corresponding_brackets[i] != latest_open_bracket.pop():
                    return False

            if i in open_brackets:
                latest_open_bracket.append(i)

        if latest_open_bracket:
            return False
        
        return True

    # def isValid(self, s: str) -> bool:
    #     """
    #     Accepted
    #     93/93 cases passed (35 ms)
    #     Your runtime beats 46.02 % of python3 submissions
    #     Your memory usage beats 15.38 % of python3 submissions (13.9 MB)
    #     """
    #     count_dict = {
    #         '(': 0,
    #         '[': 0,
    #         '{': 0
    #     }
    #     open_brackets = {'(', '[', '{'}
    #     close_brackets = {')', ']', '}'}
    #     corresponding_brackets = {
    #         '(': ')',
    #         '{': '}',
    #         '[': ']',
    #         ']': '[',
    #         '}': '{',
    #         ')': '('
    #     }
    #     latest_open_bracket = []

    #     for i in s:
    #         if i in close_brackets:
    #             if count_dict[corresponding_brackets[i]] <= 0:
    #                 return False
    #             if corresponding_brackets[i] != latest_open_bracket.pop():
    #                 return False
    #             count_dict[corresponding_brackets[i]] -= 1
    #         if i in {'(', '[', '{'}:
    #             latest_open_bracket.append(i)
    #             count_dict[i] += 1

    #     for i in open_brackets:
    #         if count_dict[i] != 0:
    #             return False
    #     return True
            

Solution().isValid('{[]}')
        
# @lc code=end

