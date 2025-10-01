from water_bottles import Solution

if __name__ == "__main__":
    numBottles = int(input("Entrez le nombre initial de bouteilles pleines : "))
    numExchange = int(input("Entrez le nombre de bouteilles vides nécessaires pour un échange : "))

    result = Solution().numWaterBottles(numBottles, numExchange)
    print("Nombre total de bouteilles bues :", result)
