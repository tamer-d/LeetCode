from remove_linked_list_elements import ListNode, Solution


def build_list(values):
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
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


if __name__ == "__main__":
    print("=== Remove Linked List Elements ===")

    values = list(map(int, input("Entrez les valeurs de la liste chaînée (séparées par des espaces) : ").split()))
    val = int(input("Entrez la valeur à supprimer : "))

    head = build_list(values)
    print("Liste avant suppression :", end=" "); print_list(head)

    sol = Solution()
    new_head = sol.removeElements(head, val)

    print("Liste après suppression :", end=" "); print_list(new_head)
