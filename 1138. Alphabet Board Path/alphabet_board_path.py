# LeetCode Problem: 1138. Alphabet Board Path
# Link: https://leetcode.com/problems/alphabet-board-path/

class Solution:
    def alphabetBoardPath(self, target):
        board = [
            "abcde",
            "fghij",
            "klmno",
            "pqrst",
            "uvwxy",
            "z"
        ]

        def find_pos(ch):
            for r in range(len(board)):
                if ch in board[r]:
                    return r, board[r].index(ch)

        res = ""
        curr_row, curr_col = 0, 0  

        for ch in target:
            row, col = find_pos(ch)

            if ch == 'z':
                while curr_col > col:
                    res += 'L'
                    curr_col -= 1
                while curr_col < col:
                    res += 'R'
                    curr_col += 1
                while curr_row < row:
                    res += 'D'
                    curr_row += 1
                while curr_row > row:
                    res += 'U'
                    curr_row -= 1
            else:
                while curr_row > row:
                    res += 'U'
                    curr_row -= 1
                while curr_row < row:
                    res += 'D'
                    curr_row += 1
                while curr_col > col:
                    res += 'L'
                    curr_col -= 1
                while curr_col < col:
                    res += 'R'
                    curr_col += 1

            res += '!'  

        return res
