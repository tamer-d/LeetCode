class Solution:
    def leastInterval(self, tasks, n):
        # Compter les fréquences manuellement
        freq = {}
        for t in tasks:
            if t in freq:
                freq[t] += 1
            else:
                freq[t] = 1

        # Trouver la fréquence max
        max_freq = 0
        for v in freq.values():
            if v > max_freq:
                max_freq = v
        
        # Compter combien ont cette fréquence
        count_max = 0
        for v in freq.values():
            if v == max_freq:
                count_max += 1
        
        # Appliquer la formule
        part1 = (max_freq - 1) * (n + 1) + count_max
        
        return max(len(tasks), part1)


if __name__ == "__main__":
    tasks = input("Entrez les tâches séparées sans espace (ex: AABAB): ")
    n = int(input("Entrez le délai n : "))
    
    sol = Solution()
    print("Temps minimal :", sol.leastInterval(list(tasks), n))
