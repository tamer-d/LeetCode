from solution import Solution

def verify_de_bruijn(s, n, k):
    need = k ** n
    seen = set()
    length = len(s)
    for i in range(length - n + 1):
        seen.add(s[i:i+n])
        if len(seen) == need:
            return True
    return len(seen) == need

if __name__ == "__main__":
    n = int(input("Entrez n (longueur des combinaisons) : "))
    k = int(input("Entrez k (alphabet 0..k-1) : "))

    sol = Solution()
    result = sol.crackSafe(n, k)

    print(f"\nGenerated sequence (length {len(result)}):")
    print(result)

    limit = 10000
    if k ** n <= limit:
        ok = verify_de_bruijn(result, n, k)
        print("\nVerification:", "OK, toutes les combinaisons sont présentes." if ok else "ÉCHEC")
        print(f"Expected distinct combos: {k**n}")
    else:
        print("\nVerification skipped (k**n is large).")
