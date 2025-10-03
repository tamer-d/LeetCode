from three_sum_closest import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez des nombres séparés par des espaces : ").split()))
    target = int(input("Entrez la valeur cible : "))
    result = Solution().threeSumClosest(nums, target)
    print("Somme la plus proche de", target, ":", result)
