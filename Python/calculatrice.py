import tkinter as tk

# Fonction pour gérer les clics sur les boutons
def bouton_click(chiffre):
    entree.insert(tk.END, chiffre)

# Fonction pour évaluer l'expression
def evaluer():
    try:
        resultat = eval(entree.get())  # Évaluer l'expression
        entree.delete(0, tk.END)  # Effacer l'entrée
        entree.insert(tk.END, str(resultat))  # Afficher le résultat
    except Exception as e:
        entree.delete(0, tk.END)
        entree.insert(tk.END, "Erreur")

# Fonction pour effacer le contenu
def effacer():
    entree.delete(0, tk.END)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.geometry("300x400")

# Zone d'entrée
entree = tk.Entry(fenetre, font=("Arial", 20), bd=8, relief=tk.SUNKEN, justify="right")
entree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Boutons numériques et opérateurs
boutons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
 
for (text, row, col) in boutons:
    if text == "=":
        bouton = tk.Button(fenetre, text=text, font=("Arial", 15), bg="lightgreen", command=evaluer)
    elif text == "C":
        bouton = tk.Button(fenetre, text=text, font=("Arial", 15), bg="red", fg="white", command=effacer)
    else:
        bouton = tk.Button(fenetre, text=text, font=("Arial", 15), command=lambda t=text: bouton_click(t))
    bouton.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Ajustement des proportions
for i in range(5):
    fenetre.rowconfigure(i, weight=1)
    fenetre.columnconfigure(i, weight=1)

# boucle principale
fenetre.mainloop()