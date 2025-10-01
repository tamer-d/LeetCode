from longest_substring import Solution

if __name__ == "__main__":
    s = input("Entrez une chaîne de caractères : ")
    result = Solution().lengthOfLongestSubstring(s)
    print("Longueur du plus long substring sans répétition :", result)
