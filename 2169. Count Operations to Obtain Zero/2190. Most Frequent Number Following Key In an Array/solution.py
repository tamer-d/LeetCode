# 2169. Count Operations to Obtain Zero

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        ops = 0
        while a and b:
            if a >= b:
                ops += a // b
                a = a % b
            else:
                ops += b // a
                b = b % a
        return ops
