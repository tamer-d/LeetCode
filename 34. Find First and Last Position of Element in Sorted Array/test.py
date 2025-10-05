from find_first_last_position import Solution

if __name__ == "__main__":
    s = Solution()

    nums = list(map(int, input("Entrez les nombres triés (séparés par des espaces) : ").split()))
    
    target = int(input("Entrez la valeur cible : "))

    result = s.searchRange(nums, target)

    print(f"\nListe : {nums}")
    print(f"Cible : {target}")
    print(f"Résultat (première et dernière position) : {result}")
