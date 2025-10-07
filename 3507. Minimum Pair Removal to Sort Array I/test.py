from minimum_pair_removal_sort_array import minimumOperations

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les valeurs du tableau nums (séparées par des espaces) : ").split()))
    res = minimumOperations(nums)
    print("Nombre minimal d’opérations :", res)
