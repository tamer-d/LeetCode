from solution import Solution

if __name__ == "__main__":

    jewels = input("Entrez les pierres précieuses (ex: aA) : ")
    stones = input("Entrez les pierres possédées (ex: aAAbbbb) : ")

    sol = Solution()
    result = sol.numJewelsInStones(jewels, stones)
    print(f"\n Nombre de pierres précieuses trouvées : {result}")
