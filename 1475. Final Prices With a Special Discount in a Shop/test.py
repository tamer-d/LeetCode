from final_prices import Solution

if __name__ == "__main__":
    prices = list(map(int, input("Entrez les prix séparés par des espaces : ").split()))
    sol = Solution()
    result = sol.finalPrices(prices)
    print("Prix finaux après remise :", result)
