from solution import minimumDistance

nums = list(
    map(int, input("Entrer les éléments du tableau séparés par espace: ").split())
)

result = minimumDistance(nums)

print("Distance minimale:", result)
