from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for string in strs:
            for char in string:
                encoding += char + char
            encoding += '01'

        return encoding

    def decode(self, s: str) -> List[str]:
        curr = ''
        decoding = []

        i = 0
        while i < len(s):
            if s[i] == '0' and s[i + 1] == '1':
                word = ''
                for j in range(len(curr) // 2):
                    word += curr[j * 2]
                decoding.append(word)
                curr = ''
                i += 2
            else:
                curr += s[i]
                i += 1

        return decoding
