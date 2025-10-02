from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for str in strs:
            letters = [0] * 26
            for char in str:
                letters[ord(char) - ord('a')] += 1
            d[tuple(letters)].append(str)

        return list(d.values())
