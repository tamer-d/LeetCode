from solution import Solution, TreeNode

#fonction tcyilna tree
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


if __name__ == "__main__":
    vals = input("Entrez les valeurs de l’arbre séparées par des espaces (None pour vide) : ").split()
    vals = [None if v == "None" else int(v) for v in vals]

    root = build_tree(vals)
    sol = Solution()
    result = sol.sumNumbers(root)

    print(f"\n Somme des nombres formés de la racine aux feuilles : {result}")
