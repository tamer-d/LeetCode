from solution import Solution

def read_edges():
    print("Entrez les arêtes sous la forme u v w (ex: 2 1 1). Tapez 'done' pour finir :")
    edges = []
    while True:
        line = input("> ").strip()
        if line.lower() == "done":
            break
        try:
            u, v, w = map(int, line.split())
            edges.append([u, v, w])
        except:
            print("Format invalide, réessayez.")
    return edges

if __name__ == "__main__":

    times = read_edges()
    n = int(input("Nombre total de nœuds : "))
    k = int(input("Nœud de départ : "))

    sol = Solution()
    result = sol.networkDelayTime(times, n, k)
    print(f"\n  Temps total minimal pour atteindre tous les nœuds : {result}")
