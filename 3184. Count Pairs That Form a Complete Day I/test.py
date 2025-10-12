from solution import Solution

if __name__ == "__main__":
    hours = list(map(int, input("Entrez les heures séparées par des espaces : ").split()))
    sol = Solution()
    result = sol.countCompleteDayPairs(hours)
    print("Nombre de paires formant une journée complète :", result)
