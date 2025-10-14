# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # on crée un dictionnaire pour compter les caractères de s
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        # on parcourt t et on retire les caractères trouvés
        for c in t:
            if c not in count or count[c] == 0:
                # c'est le caractère ajouté
                return c
            else:
                count[c] -= 1
