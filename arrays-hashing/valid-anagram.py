class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = [0] * 26
        t_letters = [0] * 26

        for char in s:
            s_letters[ord(char) - ord('a')] += 1

        for char in t:
            t_letters[ord(char) - ord('a')] += 1

        return s_letters == t_letters
