class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n 

        i = n - 1
        while k > 0 and i >= 0:
            add = min(25, k)
            res[i] = chr(ord('a') + add)
            k -= add
            i -= 1

        return ''.join(res)
    
if __name__ == "__main__":
    n = int(input("Entrez la longueur n : "))
    k = int(input("Entrez la valeur k : "))
    sol = Solution()
    print("Résultat :", sol.getSmallestString(n, k))
