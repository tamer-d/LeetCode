# LeetCode Problem: 7. Reverse Integer
# Link: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        # inversion des digits
        reversed_int = int(str(x_abs)[::-1]) * sign

        # vérifier limites 32 bits
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        return reversed_int
