# LeetCode Problem: 8. String to Integer (atoi)
# Link: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # enlever les espaces
        if not s:
            return 0

        # gérer le signe
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        # lire les chiffres
        num_str = ""
        for char in s:
            if char.isdigit():
                num_str += char
            else:
                break

        if not num_str:
            return 0

        result = sign * int(num_str)

        # clamp dans les bornes 32-bit
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
