# 3289. The Two Sneaky Numbers of Digitville

class Solution:
    def getSneakyNumbers(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # récupérer les deux nombres avec fréquence 2
        result = [x for x in count if count[x] == 2]
        return sorted(result)
