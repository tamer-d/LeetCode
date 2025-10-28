from solution import Solution

moves = input("Entrez la séquence de mouvements (ex: UDLRUD): ").strip().upper()

sol = Solution()
result = sol.judgeCircle(moves)

print(f"\nInput: moves = \"{moves}\"")
print(f"Output: {result}")

x = y = 0
for move in moves:
    if move == 'U':
        y += 1
    elif move == 'D':
        y -= 1
    elif move == 'L':
        x -= 1
    elif move == 'R':
        x += 1

print(f"Position finale du robot: ({x}, {y})")
