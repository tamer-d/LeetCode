from solution import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les nombres séparés par des espaces : ").split()))
    sol = Solution()
    result = sol.maximumPrimeDifference(nums)
    print("Résultat :", result)
