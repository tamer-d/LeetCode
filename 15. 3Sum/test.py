from three_sum import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez des nombres séparés par des espaces : ").split()))
    result = Solution().threeSum(nums)
    print("Triplets qui donnent somme = 0 :", result)
