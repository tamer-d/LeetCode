from next_greater_element import Solution

if __name__ == "__main__":
    nums1 = list(map(int, input("Entrez nums1 (séparés par des espaces) : ").split()))
    nums2 = list(map(int, input("Entrez nums2 (séparés par des espaces) : ").split()))

    sol = Solution()
    result = sol.nextGreaterElement(nums1, nums2)
    print("Résultat :", result)
