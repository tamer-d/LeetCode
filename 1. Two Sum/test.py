from two_sum import Solution

if __name__ == "__main__":
    nums_str = input("Entrez la liste des nombres (séparés par espace) : ")
    target = int(input("Entrez la valeur cible (target) : "))

    nums = list(map(int, nums_str.strip().split()))
    result = Solution().twoSum(nums, target)
    print(f"Indices trouvés : {result}")
