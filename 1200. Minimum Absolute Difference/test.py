from solution import Solution

arr = list(map(int, input("Entrez les nombres (séparés par des espaces) : ").split()))

sol = Solution()
res = sol.minimumAbsDifference(arr)

print(f"\nInput: {arr}")
print("Paires avec la différence minimale :")

for pair in res:
    print(pair)
