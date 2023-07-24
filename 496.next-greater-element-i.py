#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
from typing import List


class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     result = []
    #     lookup = {}
    #     for i, v in enumerate(nums2):
    #         lookup[v] = i
        
    #     for num in nums1:
    #         index = lookup[num]
    #         new_list = nums2[index+1:]
    #         new_list = list(filter(lambda x: x > num, new_list))
    #         if not new_list:
    #             result.append(-1)
    #         else:
    #             result.append(new_list[0])
    #     return result
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {v: i for i, v in enumerate(nums1)}
        result = [-1] * len(nums1)
        pointer = 0
        stack = []
        while pointer < len(nums2):
            curr_val = nums2[pointer]
            while stack and stack[-1] < curr_val:
                stack_val = stack.pop()
                result[lookup[stack_val]] = curr_val
            if curr_val in lookup:
                stack.append(curr_val)
            pointer += 1

        # while stack:
        #     stack_val = stack.pop()
        #     if lookup.get(stack_val) != None:
        #         nums1[lookup[stack_val]] = -1
        return result
        

# @lc code=end
a = Solution().nextGreaterElement([137, 59, 92, 122, 52, 131], [
    137, 59, 92, 122, 52, 131, 236, 94])
print(a)
