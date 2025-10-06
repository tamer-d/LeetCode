from rotate_list import ListNode, Solution

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
    k = int(input("Entrez k (le nombre de rotations) : "))
    
    head = build_list(values)
    sol = Solution()
    new_head = sol.rotateRight(head, k)
    
    print("Liste après rotation :")
    print_list(new_head)
