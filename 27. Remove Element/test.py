from remove_element import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les nombres séparés par des espaces : ").split()))
    val = int(input("Entrez la valeur à supprimer : "))
    k = Solution().removeElement(nums, val)
    print("Nouvelle longueur :", k)
    print("Tableau modifié :", nums[:k])
