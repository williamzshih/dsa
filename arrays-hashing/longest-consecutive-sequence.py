from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in s:
                length = 1
                curr = num + 1
                while curr in s:
                    length += 1
                    curr += 1
                max_length = max(max_length, length)

        return max_length
