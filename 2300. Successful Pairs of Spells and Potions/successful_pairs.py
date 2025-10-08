# LeetCode 2300. Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            min_needed = (success + spell - 1) // spell

            left = 0
            right = n - 1
            index = n  

            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= min_needed:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(n - index)

        return result
