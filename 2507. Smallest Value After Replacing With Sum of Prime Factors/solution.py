# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def sum_prime_factors(x):
            s = 0
            d = 2
            while d * d <= x:
                while x % d == 0:
                    s += d
                    x //= d
                d += 1
            if x > 1:
                s += x
            return s

        prev = -1
        while n != prev:
            prev = n
            n = sum_prime_factors(n)
        return n
