# LeetCode Problem: 1475. Final Prices With a Special Discount in a Shop
# Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        res = prices[:]  
        stack = []  

        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                res[idx] = prices[idx] - prices[i]
            stack.append(i)

        return res