class Solution:
    def reorganizeString(self, s):
        n = len(s)
        # Compter les fréquences (avec une simple boucle)
        freq = []
        for c in set(s):
            freq.append([c, s.count(c)])
        
        # Trier par fréquence décroissante
        freq.sort(key=lambda x: -x[1])
        
        # Vérifier la condition d'impossibilité
        if freq[0][1] > (n + 1) // 2:
            return ""
        
        res = [""] * n
        i = 0  # index pour placer les caractères
        
        # Remplir le tableau
        for char, count in freq:
            for _ in range(count):
                res[i] = char
                i += 2
                if i >= n:
                    i = 1  # passer aux indices impairs
        
        return "".join(res)


if __name__ == "__main__":
    s = input("Entrez la chaîne : ")
    sol = Solution()
    print("Résultat :", sol.reorganizeString(s))
