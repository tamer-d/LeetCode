from solution import Solution

if __name__ == "__main__":
    g = list(map(int, input("Entrez les appétits des enfants : ").split()))
    s = list(map(int, input("Entrez les tailles des cookies : ").split()))

    sol = Solution()
    result = sol.findContentChildren(g, s)

    print(f"\n Nombre maximum d'enfants satisfaits : {result}")
