from find_index_first_occurrence import Solution

if __name__ == "__main__":
    haystack = input("Entrez le texte (haystack) : ")
    needle = input("Entrez le motif (needle) : ")
    result = Solution().strStr(haystack, needle)
    print("Index de la première occurrence :", result)
