from solution import Solution

if __name__ == "__main__":

    a = int(input("Entrez num1 : ").strip())
    b = int(input("Entrez num2 : ").strip())

    sol = Solution()
    result = sol.countOperations(a, b)

    print(f"\nInput: num1 = {a}, num2 = {b}")
    print(f"Output: {result}")
