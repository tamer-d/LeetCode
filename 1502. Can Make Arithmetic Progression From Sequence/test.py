
from solution import Solution

if __name__ == "__main__":
    arr = list(map(int, input("Entrez la liste des nombres (séparés par des espaces) : ").split()))
    
    sol = Solution()
    result = sol.canMakeArithmeticProgression(arr)

    print(f"\n On peut former une progression arithmétique? : {result}")
