from daily_temperatures import Solution

if __name__ == "__main__":
    temps = list(map(int, input("Entrez les températures séparées par des espaces : ").split()))

    sol = Solution()
    result = sol.dailyTemperatures(temps)

    print("Résultat :", result)