from solution import maxRotateFunction

nums = list(map(int, input("Entrer les éléments du tableau: ").split()))

result = maxRotateFunction(nums)

print("Valeur maximale:", result)
