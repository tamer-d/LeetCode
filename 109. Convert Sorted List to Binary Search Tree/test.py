from convert_sorted_list_to_bst import ListNode, Solution

def build_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head
def print_tree(node, level=0):
    if not node:
        return
    print_tree(node.right, level + 1)
    print('   ' * level + f"-> {node.val}")
    print_tree(node.left, level + 1)

if __name__ == "__main__":
    values = list(map(int, input("Entrez les valeurs triées de la liste séparées par des espaces : ").split()))
    
    head = build_list(values)
    sol = Solution()
    bst_root = sol.sortedListToBST(head)
    
    print("\nArbre binaire de recherche équilibré :")
    print_tree(bst_root)
