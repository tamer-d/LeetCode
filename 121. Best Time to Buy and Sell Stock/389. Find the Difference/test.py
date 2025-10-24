from solution import Solution

prices = list(map(int, input("Entrez les prix journaliers de l'action : ").split()))

sol = Solution()
result = sol.maxProfit(prices)

print(f"\n Profit maximum possible : {result}")
