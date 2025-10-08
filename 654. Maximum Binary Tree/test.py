from maximum_binary_tree import Solution

def print_tree(node, level=0):
    """Affichage simple de l’arbre (rotation à 90°)"""
    if node is not None:
        print_tree(node.right, level + 1)
        print('    ' * level + f'-> {node.val}')
        print_tree(node.left, level + 1)

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les nombres séparés par des espaces : ").split()))

    sol = Solution()
    root = sol.constructMaximumBinaryTree(nums)

    print("\nArbre binaire construit :\n")
    print_tree(root)
