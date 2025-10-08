from min_stack import MinStack

if __name__ == "__main__":
    stack = MinStack()

    while True:
        print("\nChoisir une opération :")
        print("1. push()")
        print("2. pop()")
        print("3. top()")
        print("4. getMin()")
        print("5. afficher la pile")
        print("0. quitter")

        choix = input("\n→ ")

        if choix == "1":
            val = int(input("Entrez une valeur à empiler : "))
            stack.push(val)
            print(f"{val} ajouté à la pile.")
        elif choix == "2":
            stack.pop()
            print("Élément retiré.")
        elif choix == "3":
            print("Sommet de la pile :", stack.top())
        elif choix == "4":
            print("Minimum actuel :", stack.getMin())
        elif choix == "5":
            print("Pile :", stack.stack)
        elif choix == "0":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide.")
