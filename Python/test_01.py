import tkinter as tk
from tkinter import messagebox


# Fonction de vérification
def verification(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()

    # Login et mot de passe valides
    valid_username = "admin"
    valid_password = "1234"

    if username == valid_username and password == valid_password:
        messagebox.showinfo("Succès", "Connexion réussie. Bienvenue!")
        login_window.destroy()  # Ferme la fenêtre de login
        show_home_page()  # Affiche la page d'accueil
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")


# Page de connexion
def login():
    global login_window

    root.withdraw()  # Masquer la fenêtre principale
    login_window = tk.Toplevel(root)  # Créer une nouvelle fenêtre
    login_window.title("Page Login")
    login_window.geometry("400x300")

    # Widgets de connexion
    tk.Label(login_window, text="Nom d'utilisateur:", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Mot de passe:", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    tk.Button(
        login_window,
        text="Se connecter",
        command=lambda: verification(username_entry, password_entry),
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12),
    ).pack(pady=20)

    # Bouton pour revenir à la page principale
    tk.Button(
        login_window,
        text="Retour",
        command=lambda: back_to_main(login_window),
        bg="#f44336",
        fg="white",
        font=("Arial", 12),
    ).pack(pady=10)


# Page d'accueil après connexion
def show_home_page():
    home_window = tk.Toplevel(root)
    home_window.title("Page d'accueil")
    home_window.geometry("400x300")

    tk.Label(home_window, text="Bienvenue sur la page d'accueil!", font=("Arial", 14)).pack(pady=20)
    tk.Button(home_window, text="Quitter", command=root.quit, bg="#f44336", fg="white", font=("Arial", 12)).pack(pady=20)


# Retour à la page principale
def back_to_main(window):
    window.destroy()
    root.deiconify()  # Affiche à nouveau la fenêtre principale


# Fenêtre principale
root = tk.Tk()
root.title("Page principale")
root.geometry("300x200")

tk.Button(root, text="Login", command=login, bg="#2196f3", fg="white", font=("Arial", 14)).pack(pady=50)

root.mainloop()
