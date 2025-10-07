from split_linked_list_in_parts import ListNode, Solution


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def print_parts(parts):
    for i, head in enumerate(parts):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        print(f"Part {i+1}: {vals}")


if __name__ == "__main__":
    print("=== Split Linked List in Parts ===")

    values = list(map(int, input("Entrez les valeurs de la liste chaînée (séparées par des espaces) : ").split()))
    k = int(input("Entrez la valeur de k : "))

    head = build_list(values)
    sol = Solution()
    parts = sol.splitListToParts(head, k)

    print("\nRésultat :")
    print_parts(parts)
