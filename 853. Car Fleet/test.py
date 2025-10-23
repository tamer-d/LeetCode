from solution import Solution

if __name__ == "__main__":
    target = int(input("Entrez la position de la cible : "))
    position = list(map(int, input("Entrez les positions des voitures : ").split()))
    speed = list(map(int, input("Entrez les vitesses des voitures : ").split()))

    sol = Solution()
    result = sol.carFleet(target, position, speed)

    print(f"\n Nombre total de flottes de voitures : {result}")
