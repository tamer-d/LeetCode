from solution import Solution

def main():

    apple = list(map(int, input("Entrez les pommes (ex: 1 3 2): ").split()))
    capacity = list(map(int, input("Entrez les capacités (ex: 4 3 1 5): ").split()))

    sol = Solution()
    result = sol.minimumBoxes(apple, capacity)

    print("Nombre minimum de boites nécessaires :", result)

if __name__ == "__main__":
    main()
