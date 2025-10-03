from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r]

                if sum == -num:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum > -num:
                    r -= 1
                elif sum < -num:
                    l += 1

        return res
