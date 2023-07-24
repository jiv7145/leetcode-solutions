#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start

import re

class Solution:
    def decodeString(self, s: str) -> str:
        def find(s) -> tuple[int, int, int, str]: # result[2] returns -1 if not found
            #return starting_index, ending_index, multiplier
            match = re.search(r"[0-9]+\[", s)
            if not match:
                return (-1, -1, -1, '')
            
            multiplier = int(match.group()[:-1])
            start_index = match.start()
            end_index = -1
            stack = []
            i = start_index
            start_index_bracket = start_index + len(match.group()) - 1
            
            while i < len(s):
                if s[i] == '[':
                    stack.append('[')
                elif s[i] == ']':
                    stack.pop()
                    if not stack:
                        end_index = i
                        break
                i += 1
            
            bracket_contents = s[start_index_bracket+1:end_index]
            return (start_index, end_index, multiplier, bracket_contents)

        str_copy = s
        info = find(str_copy)
        while info[2] != -1:
            (start_index, end_index, multiplier, str_in_bracket) = info
            decoded_str = multiplier * str_in_bracket
            str_copy = str_copy[:start_index] + decoded_str + str_copy[end_index+1:]
            info = find(str_copy)
        
        return str_copy
# @lc code=end

