#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        processed_nums = []

        prev_elem = nums[0]
        count = 0

        for index, num in enumerate(nums):
            if prev_elem == num:
                count += 1
                if index == len(nums) - 1:
                    processed_nums.append(count)
            else:
                prev_elem = num
                processed_nums.append(count)
                count = 1
                if index == len(nums) - 1:
                    processed_nums.append(1)

        starting_index = 0 if nums[0] == 0 else 1
        longest = 0

        more_zeroes = set()
        for i in range(starting_index, len(processed_nums), 2):
            current_zeroes = processed_nums[i]
            if current_zeroes > k:
                more_zeroes.add(i)
                continue
            
            if i - 1 < 0:
                longest_length = processed_nums[i+1]
            elif i + 1 >= len(processed_nums):
                longest_length = processed_nums[i-1]
            else:
                longest_length = processed_nums[i - 1] + processed_nums[i + 1]
            
            num_of_slots = k - current_zeroes
            ind = i + 2
            while ind < len(processed_nums) and num_of_slots > 0:
                new_zeroes = processed_nums[ind]
                num_of_slots -= new_zeroes
                if num_of_slots >= 0 and ind + 1 < len(processed_nums):
                    longest_length += processed_nums[ind+1]
                ind += 2

            if longest_length > longest:
                longest = longest_length + k

        new_starting_index = starting_index ^ 1

        # [3,3,4,1]
        for i in range(new_starting_index, len(processed_nums), 2):
            if longest < processed_nums[i] + k:
                longest = processed_nums[i] + k

        return longest


# @lc code=end
a = Solution().longestOnes(
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
print(a)
