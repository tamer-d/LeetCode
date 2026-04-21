from solution import minimumHammingDistance

source = list(map(int, input("Entrer source: ").split()))
target = list(map(int, input("Entrer target: ").split()))

m = int(input("Nombre de swaps autorisés: "))

allowedSwaps = []

for _ in range(m):
    a, b = map(int, input("Entrer un swap (i j): ").split())
    allowedSwaps.append([a, b])


result = minimumHammingDistance(source, target, allowedSwaps)

print("Distance de Hamming minimale:", result)
