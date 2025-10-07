from browser_history import BrowserHistory

if __name__ == "__main__":
    print("=== Simulation du navigateur ===")
    homepage = input("Entrez la page d'accueil : ")
    browser = BrowserHistory(homepage)

    while True:
        action = input("\nAction (visit/back/forward/show/exit) : ").strip().lower()
        
        if action == "visit":
            url = input("Entrez l'URL à visiter : ")
            browser.visit(url)
            print(f"→ Vous êtes sur : {browser.history[browser.current]}")
        
        elif action == "back":
            steps = int(input("Combien d'étapes en arrière ? "))
            print(f"→ Vous êtes sur : {browser.back(steps)}")
        
        elif action == "forward":
            steps = int(input("Combien d'étapes en avant ? "))
            print(f"→ Vous êtes sur : {browser.forward(steps)}")
        
        elif action == "show":
            print("Historique :", browser.history)
            print(f"Page actuelle → {browser.history[browser.current]}")
        
        elif action == "exit":
            print("Fermeture du navigateur.")
            break
        
        else:
            print("Commande invalide. Essayez : visit, back, forward, show, exit")
