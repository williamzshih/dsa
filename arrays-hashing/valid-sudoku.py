from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == '.':
                    continue
                if char in row_sets[i]:
                    return False
                if char in col_sets[j]:
                    return False
                if char in box_sets[i // 3 * 3 + j // 3]:
                    return False
                row_sets[i].add(char)
                col_sets[j].add(char)
                box_sets[i // 3 * 3 + j // 3].add(char)

        return True
