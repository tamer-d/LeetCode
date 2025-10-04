from container_with_most_water import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les hauteurs séparées par des espaces : ").split()))
    result = Solution().maxArea(nums)
    print("La capacité maximale d'eau est :", result)
