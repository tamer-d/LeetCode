from solution import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez la liste nums (espaces entre nombres) : ").split()))
    key = int(input("Entrez la valeur de key : "))

    sol = Solution()
    result = sol.mostFrequent(nums, key)

    print("\n Le nombre le plus fréquent après", key, "est :", result)
