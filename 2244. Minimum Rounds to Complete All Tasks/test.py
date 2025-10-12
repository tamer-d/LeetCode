from solution import Solution

if __name__ == "__main__":
    tasks = list(map(int, input("Entrez les tâches séparées par des espaces : ").split()))
    sol = Solution()
    result = sol.minimumRounds(tasks)
    print("Nombre minimum de rounds nécessaires :", result)
