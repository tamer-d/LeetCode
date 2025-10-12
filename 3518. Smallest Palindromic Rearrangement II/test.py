from solution import Solution

if __name__ == "__main__":
    s = input("Entrez la chaîne palindromique s : ")
    k = int(input("Entrez k : "))
    sol = Solution()
    res = sol.smallestPalindrome(s, k)
    if res == "":
        print("Pas de palindrome k-ème possible.")
    else:
        print("Le", k, "-ème palindrome lexico minimal est :", res)
