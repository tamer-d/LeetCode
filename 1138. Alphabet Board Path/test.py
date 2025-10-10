from alphabet_board_path import Solution

if __name__ == "__main__":

    target = input("Entrez le mot cible (en miniscules) : ").strip()
    sol = Solution()
    print("Chemin :", sol.alphabetBoardPath(target))
