from intersection_of_two_linked_lists import ListNode, Solution


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
    print("=== Intersection of Two Linked Lists ===")

    # Saisie des listes
    listA_vals = list(map(int, input("Entrez les valeurs de la liste A (séparées par des espaces) : ").split()))
    listB_vals = list(map(int, input("Entrez les valeurs de la liste B (séparées par des espaces) : ").split()))
    common_vals = list(map(int, input("Entrez les valeurs de la partie commune (si aucune, laissez vide et appuyez sur Entrée) : ").split() or []))

    # Construction des listes
    intersect = build_list(common_vals) if common_vals else None

    headA = build_list(listA_vals)
    headB = build_list(listB_vals)

    # Relier la partie commune
    if intersect:
        currA = headA
        while currA and currA.next:
            currA = currA.next
        currA.next = intersect

        currB = headB
        while currB and currB.next:
            currB = currB.next
        currB.next = intersect

    print("\nListe A : ", end=""); print_list(headA)
    print("Liste B : ", end=""); print_list(headB)

    sol = Solution()
    inter = sol.getIntersectionNode(headA, headB)

    print("\n→ Nœud d'intersection :", inter.val if inter else "Aucun")
