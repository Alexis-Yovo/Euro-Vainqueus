print("Vainqueurs du Championnat d'Europe de football (Euro)")

while True:
    choice = input("Citez un pays vainqueur de l'Euro: ").lower()
    match(choice):
        case "union soviétique" | "urss" | "russie":
            print("L'Union soviétique a gagné l'Euro en 1960.")
        case "espagne":
            print("L'Espagne a gagné l'Euro en 1964, en 2008, en 2012 et en 2024.")
        case "italie":
            print("L'Italie a gagné l'Euro en 1968 et en 2021.")
        case "allemagne":
            print("L'Allemagne a gagné l'Euro en 1972, en 1980 et en 1996.")
        case "france":
            print("La France a gagné l'Euro en 1984 et en 2000.")
        case "hollande" | "pays-bas":
            print("Les Pays-Bas ont gagné l'Euro en 1988.")
        case "danemark":
            print("Le Danemark a gagné l'Euro en 1992.")
        case "grèce":
            print("La Grèce a gagné l'Euro en 2004.")
        case "portugal":
            print("Le Portugal a gagné l'Euro en 2016.")
        case "tchécoslovaquie" | "république tchèque" | "tchéquie" | "slovaquie":
            print("La Tchécoslovaquie a gagné l'Euro en 1976.")
        case _:
            print("Erreur 404")
