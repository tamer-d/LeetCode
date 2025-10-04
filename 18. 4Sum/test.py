from four_sum import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez des nombres séparés par des espaces : ").split()))
    target = int(input("Entrez la valeur cible : "))
    result = Solution().fourSum(nums, target)
    print("Quadruplets qui donnent somme =", target, ":", result)
