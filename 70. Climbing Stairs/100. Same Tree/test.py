from solution import Solution

n = int(input("Entrez le nombre de marches : "))

sol = Solution()
res = sol.climbStairs(n)

print(f"\nNombre de façons de monter {n} marches : {res}")
