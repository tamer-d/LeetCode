# 3354. Make Array Elements Equal to Zero

class Solution:
    def minimumOperations(self, nums):
        steps = []
        nums = nums[:] 
        count = 0

        while True:
            positives = [x for x in nums if x > 0]
            if not positives:
                break

            m = min(positives)
            nums = [x - m if x > 0 else 0 for x in nums]
            count += 1
            steps.append((m, nums[:]))

        return count, steps