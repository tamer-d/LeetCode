# 888. Fair Candy Swap

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) // 2
        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x - diff in bobSet:
                return [x, x - diff]
        return []