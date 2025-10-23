from solution import Solution

if __name__ == "__main__":

    n = int(input("Entrez le nombre de types de boîtes : "))
    boxTypes = []
    
    for i in range(n):
        print(f"Type {i+1} :")
        numberOfBoxes = int(input("  Nombre de boîtes : "))
        unitsPerBox = int(input("  Unités par boîte : "))
        boxTypes.append([numberOfBoxes, unitsPerBox])
    
    truckSize = int(input("\nEntrez la capacité du camion (en nombre de boîtes) : "))

    sol = Solution()
    result = sol.maximumUnits(boxTypes, truckSize)

    print(f"\n🚛 Nombre maximum d'unités transportées : {result}")
