from spiral_matrix_ii import Solution

if __name__ == "__main__":
    n = int(input("Entrez la taille n de la matrice : "))
    result = Solution().generateMatrix(n)
    
    print("\nMatrice en spirale :")
    for row in result:
        print(row)
