#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
import math
from typing import List


class Solution:
    # def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    #     def distance(p1, p2):
    #         return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    #     distances = [(i, distance(point, [0, 0])) for i, point in enumerate(points)]
    #     distances.sort(key=lambda x: x[1])
    #     distances = distances[:k]
    #     return [points[index] for index, _ in distances]
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(p1, p2):
            return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

        distances = [(distance(point, [0, 0]), i)
                     for i, point in enumerate(points)]
        
        heapq.heapify(distances)
        res = []
        while k > 0:
            dist, index = heapq.heappop(distances)
            res.append(index)
            k -= 1
        return [points[i] for i in res]
        
        
# @lc code=end



