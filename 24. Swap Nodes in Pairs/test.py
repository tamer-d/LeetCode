from swap_nodes_in_pairs import Solution, ListNode

def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    values = list(map(int, input("Entrez les valeurs de la liste (séparées par des espaces) : ").split()))

    head = build_linked_list(values)
    result = Solution().swapPairs(head)

    print("\nAvant permutation :", values)
    print("Après permutation  :", linked_list_to_list(result))
