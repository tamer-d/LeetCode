from remove_nth_node_from_end import ListNode, Solution

def build_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

if __name__ == "__main__":
    values = list(map(int, input("Entrez les valeurs de la liste séparées par des espaces : ").split()))
    n = int(input("Entrez n (la position à supprimer depuis la fin) : "))
    
    head = build_list(values)
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    
    print("Nouvelle liste après suppression :")
    print_list(new_head)
