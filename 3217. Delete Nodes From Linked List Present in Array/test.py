from delete_nodes_from_linked_list_present_in_array import ListNode, Solution

def build_list(values):
    """Construit une liste chaînée depuis une liste Python."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next
    print(vals)

if __name__ == "__main__":
    print("=== Delete Nodes From Linked List Present in Array ===")
    nums = list(map(int, input("Entrez les valeurs du tableau nums (séparées par des espaces) : ").split()))
    values = list(map(int, input("Entrez les valeurs de la liste chaînée (séparées par des espaces) : ").split()))
    
    head = build_list(values)
    sol = Solution()
    new_head = sol.modifiedList(nums, head)
    
    print("Liste après suppression :", end=" ")
    print_list(new_head)
