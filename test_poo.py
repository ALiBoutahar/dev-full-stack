import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice d'Addition")

        # Champ de saisie pour le premier nombre
        tk.Label(root, text="Nombre 1:").grid(row=0, column=0, padx=10, pady=10)
        self.num1_entry = tk.Entry(root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        # Champ de saisie pour le deuxième nombre
        tk.Label(root, text="Nombre 2:").grid(row=1, column=0, padx=10, pady=10)
        self.num2_entry = tk.Entry(root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        # Bouton pour calculer l'addition
        self.calculate_button = tk.Button(root, text="Calculer", command=self.calculate_sum)
        self.calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

    def calculate_sum(self):
        try:
            # Récupération des nombres saisis
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            result = num1 + num2

            # Affichage du résultat
            messagebox.showinfo("Résultat", f"La somme est : {result}")
        except ValueError:
            # Gestion des erreurs si les entrées ne sont pas valides
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")

# Point d'entrée principal
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
