from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]] * len(height)
        postfix = [height[-1]] * len(height)

        for i in range(1, len(height)):
            prefix[i] = max(height[i], prefix[i - 1])

        for i in range(len(height) - 2, -1, -1):
            postfix[i] = max(height[i], postfix[i + 1])

        water = 0

        for i in range(1, len(height) - 1):
            area = min(prefix[i - 1], postfix[i + 1]) - height[i]
            if area > 0:
                water += area

        return water
