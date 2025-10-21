from solution import Solution

if __name__ == "__main__":
    coins = list(map(int, input("Entrez les valeurs des pièces séparées par des espaces : ").split()))
    amount = int(input("Entrez le montant à former : "))

    sol = Solution()
    result = sol.coinChange(coins, amount)

    if result == -1:
        print("\n Impossible de former ce montant avec les pièces données.")
    else:
        print(f"\n Nombre minimum de pièces nécessaires : {result}")
