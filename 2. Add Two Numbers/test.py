from add_two_numbers import Solution, ListNode

def build_linked_list(numbers):
    """Convertit une liste [2,4,3] en liste chaînée 2->4->3"""
    dummy = ListNode(0)
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    """Convertit une liste chaînée en liste Python"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    nums1 = list(map(int, input("Entrez la 1ère liste (ex: 2 4 3): ").split()))
    nums2 = list(map(int, input("Entrez la 2ème liste (ex: 5 6 4): ").split()))

    l1 = build_linked_list(nums1)
    l2 = build_linked_list(nums2)

    result = Solution().addTwoNumbers(l1, l2)
    print("Résultat :", linked_list_to_list(result))
