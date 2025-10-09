from find_the_minimum_amount_of_time_to_brew_potions import Solution

if __name__ == "__main__":
    skill = list(map(int, input("Entrez les compétences des sorciers (skill) séparées par des espaces : ").split()))
    mana = list(map(int, input("Entrez les puissances des potions (mana) séparées par des espaces : ").split()))

    sol = Solution()
    result = sol.minTime(skill, mana)
    print("Temps minimal total :", result)
