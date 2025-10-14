from solution import Solution

if __name__ == "__main__":
    s = input("Entrez la première chaîne s : ")
    t = input("Entrez la deuxième chaîne t (avec une lettre ajoutée) : ")

    sol = Solution()
    result = sol.findTheDifference(s, t)
    print(f"\n La lettre ajoutée est : '{result}'")
