from solution import Solution, ListNode

def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

vals = list(map(int, input("Entrez les valeurs de la liste séparées par espace : ").split()))
x = int(input("Entrez x : "))

head = build_list(vals)
sol = Solution()
res = sol.partition(head, x)

print("\nListe partitionnée :")
print_list(res)
