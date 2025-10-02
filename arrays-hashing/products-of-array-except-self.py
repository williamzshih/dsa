from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(len(nums)):
            prefix[i] = nums[i] * (1 if i - 1 < 0 else prefix[i - 1])
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = nums[j] * \
                (1 if j + 1 >= len(nums) else postfix[j + 1])

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = (1 if i - 1 < 0 else prefix[i - 1]) * \
                (1 if i + 1 >= len(nums) else postfix[i + 1])

        return res
