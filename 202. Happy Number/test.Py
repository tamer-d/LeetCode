from solution import Solution

if __name__ == "__main__":
    sol = Solution()
    n = int(input("Entrez un nombre entier : "))
    result = sol.isHappy(n)
    if result:
        print(f"{n} est heureux !")
    else:
        print(f"{n} n'est pas heureux.")
