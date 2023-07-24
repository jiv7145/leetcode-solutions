#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
from typing import List


class Solution:
    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     for target in [tops[0], bottoms[0]]:
    #         missingT, missingB = 0, 0
    #         for i, pair in enumerate(zip(tops, bottoms)):
    #             top, bottom = pair
    #             if not (top == target or bottom == target):
    #                 break
    #             if top != target:
    #                 missingT += 1
    #             if bottom != target:
    #                 missingB += 1
    #             if i == len(tops) - 1:
    #                 return min(missingT, missingB)
    #     return -1


    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top, bottom = tops[0], bottoms[0]

        occ_top, occ_bottom = 0, 0
        #assuming common number is tops[0]
        for i in range(len(tops)):
            if not (top == tops[i] or top == bottoms[i]):
                break
            if tops[i] != top:
                occ_top += 1
            if bottoms[i] != top:
                occ_bottom += 1
            if i == len(tops) - 1:
                return min(occ_top, occ_bottom)
        
        occ_top, occ_bottom = 0, 0
        for i in range(len(tops)):
            if not (bottom == tops[i] or bottom == bottoms[i]):
                break
            if tops[i] != bottom:
                occ_top += 1
            if bottoms[i] != bottom:
                occ_bottom += 1
            if i == len(tops) - 1:
                return min(occ_top, occ_bottom)
        return -1
            

    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     # find the common number that occurs in all columns
    #     top = tops[0]
    #     bottom = bottoms[0]

    #     s = {top, bottom}
    #     common_num = -1
        
    #     is_only_one_or_two_numbers = True
    #     is_only_one_number = True
    #     for i in range(len(tops)):
    #         if tops[i] != bottoms[i]:
    #             is_only_one_number = False

    #     if is_only_one_number:
    #         return 0
        
    #     for i in range(len(tops)):
    #         if tops[i] not in s or bottoms[i] not in s:
    #             is_only_one_or_two_numbers = False
    #     swaps = 0
    #     if is_only_one_or_two_numbers: # only two numbers
    #         first_num = -1
    #         second_num = -1
    #         for i in range(len(tops)):
    #             if tops[i] != bottoms[i]:
    #                 first_num, second_num = tops[i], bottoms[i]
    #             if i == len(tops) - 1 and first_num == -1:
    #                 return 0
            
    #         store = {
    #             'top_first_num_occ': tops.count(first_num),
    #             'top_second_num_occ': tops.count(second_num),
    #             'bottom_first_num_occ': bottoms.count(first_num),
    #             'bottom_second_num_occ': bottoms.count(second_num)
    #         }
    #         max_occ = max(store, key=store.get)
    #         return len(tops) - store[max_occ]



    #     # TODO include a case where both top and bottom is in set
    #     if tops[1] in s:
    #         common_num = tops[1]
    #     elif bottoms[1] in s:
    #         common_num = bottoms[1]

        
    #     occurances_on_top = tops.count(common_num)
    #     occurances_on_bottom = bottoms.count(common_num)

        
    #     for i in range(len(tops)):
    #         if tops[i] != common_num and bottoms[i] != common_num:
    #             return -1

    #     if occurances_on_top > occurances_on_bottom:
    #         return len(tops) - occurances_on_top
    #     else:
    #         return len(bottoms) - occurances_on_bottom

    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     def check(x):
    #         """
    #         This helper function checks number of rotations if we make number x on top of every domino.
    #         If it's not possible to make number x on top of every domino, it returns -1.
    #         """
    #         rotations_top = rotations_bottom = 0
    #         for i in range(len(tops)):
    #             # If number x is not present on either top or bottom, return -1
    #             if tops[i] != x and bottoms[i] != x:
    #                 return -1
    #             # Count rotations
    #             elif tops[i] != x:
    #                 rotations_top += 1
    #             elif bottoms[i] != x:
    #                 rotations_bottom += 1
    #         # Min number of rotations to have all values x in top or bottom
    #         return min(rotations_top, rotations_bottom)

    #     rotations = check(tops[0])
    #     # If one could make all elements in tops or bottoms array to be equal to tops[0]
    #     if rotations != -1 or tops[0] == bottoms[0]:
    #         return rotations
    #     # If one could make all elements in tops or bottoms array to be equal to bottoms[0]
    #     else:
    #         return check(bottoms[0])

# @lc code=end
Solution().minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2])