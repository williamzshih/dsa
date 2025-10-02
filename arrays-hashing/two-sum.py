from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(nums):
            other = target - num
            if other in d:
                return [d[other], i]
            d[num] = i
