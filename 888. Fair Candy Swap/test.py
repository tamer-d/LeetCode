from solution import Solution

if __name__ == "__main__":

    alice = list(map(int, input("Entrez les tailles des bonbons d'Alice : ").split()))
    bob = list(map(int, input("Entrez les tailles des bonbons de Bob : ").split()))

    sol = Solution()
    result = sol.fairCandySwap(alice, bob)

    print(f"\n Échange équitable : {result[0]} (Alice) ↔ {result[1]} (Bob)")
