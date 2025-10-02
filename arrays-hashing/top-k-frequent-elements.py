from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        l = [[] for _ in range(len(nums))]
        for num in d:
            l[d[num] - 1].append(num)

        p = len(nums) - 1
        res = []

        while True:
            if l[p]:
                for num in l[p]:
                    res.append(num)
                    k -= 1
                    if k == 0:
                        return res
                p -= 1
            else:
                p -= 1
