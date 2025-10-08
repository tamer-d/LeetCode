from valid_parenthesis_string import Solution

if __name__ == "__main__":
    s = input("Entrez une chaîne contenant (, ), * : ")

    sol = Solution()
    result = sol.checkValidString(s)

    print("\nChaîne valide ?" , result)
