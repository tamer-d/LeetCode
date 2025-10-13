class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []  

        while n != 1:
            if n in seen:  
                return False
            seen.append(n)

            total = 0
            for digit in str(n):
                total += int(digit) ** 2  
            n = total  

        return True  
