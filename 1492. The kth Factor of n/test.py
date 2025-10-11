from solution import Solution

if __name__ == "__main__":
    n = int(input("Entrez la valeur de n : "))
    k = int(input("Entrez la valeur de k : "))
    sol = Solution()
    result = sol.kthFactor(n, k)
    print("\nLe", k, "ᵉ facteur de", n, "est :", result)
