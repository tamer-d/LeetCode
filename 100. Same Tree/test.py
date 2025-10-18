from solution import Solution, TreeNode

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

    list1 = input("Entrez les valeurs du premier arbre séparées par des espaces (utilisez None pour vide) : ").split()
    list2 = input("Entrez les valeurs du deuxième arbre séparées par des espaces (utilisez None pour vide) : ").split()

    vals1 = [None if v == "None" else int(v) for v in list1]
    vals2 = [None if v == "None" else int(v) for v in list2]

    p = build_tree(vals1)
    q = build_tree(vals2)

    sol = Solution()
    result = sol.isSameTree(p, q)

    print(f"\n Les deux arbres sont-ils identiques ? {result}")
