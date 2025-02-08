import tkinter as tk
from tkinter import messagebox

# base de Données utilisateur simulées
users_db = {}

# Fonction de vérification des identifiants
def verify_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users_db and users_db[username] == password:
        open_main_page(username)
    else:
        messagebox.showerror("Erreur", "Login ou mot de passe incorrect")

# Fonction d'inscription
def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()
    confirm_password = reg_confirm_password_entry.get()
    
    if username in users_db:
        messagebox.showerror("Erreur", "Nom d'utilisateur déjà existant")
    elif password != confirm_password:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
    elif len(password) < 4:
        messagebox.showerror("Erreur", "Le mot de passe doit contenir au moins 4 caractères")
    else:
        users_db[username] = password
        messagebox.showinfo("Succès", "Inscription réussie ! Vous pouvez vous connecter.")
        show_login_page()

# Fonction pour afficher la page d'inscription
def show_register_page():
    login_frame.pack_forget()
    register_frame.pack(pady=20)

# Fonction pour afficher la page de connexion
def show_login_page():
    register_frame.pack_forget()
    login_frame.pack(pady=20)

# Fonction pour ouvrir la page principale après connexion
def open_main_page(username):
    root.withdraw()
    main_window = tk.Toplevel()
    main_window.title("Page principale")
    main_window.geometry("400x300")
    main_window.configure(bg="#f0f8ff")

    tk.Label(main_window, text=f"Bienvenue, {username}!", font=("Arial", 16), bg="#f0f8ff").pack(pady=20)
    
    # Section de calcul
    calc_frame = tk.Frame(main_window, bg="#f0f8ff")
    calc_frame.pack(pady=20)
    
    tk.Label(calc_frame, text="Nombre 1:", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5)
    num1_entry = tk.Entry(calc_frame)
    num1_entry.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(calc_frame, text="Nombre 2:", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5)
    num2_entry = tk.Entry(calc_frame)
    num2_entry.grid(row=1, column=1, padx=5, pady=5)
    
    result_label = tk.Label(calc_frame, text="Résultat: ", bg="#f0f8ff")
    result_label.grid(row=2, column=0, columnspan=2, pady=5)
    
    def calculate():
        try:
            num1 = float(num1_entry.get())
            num2 = float(num2_entry.get())
            result = num1 + num2
            result_label.config(text=f"Résultat: {result}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")
    
    calc_button = tk.Button(calc_frame, text="Calculer", command=calculate, bg="#4caf50", fg="white")
    calc_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    # Bouton pour fermer
    close_button = tk.Button(main_window, text="Se déconnecter", command=lambda: main_window.destroy())
    close_button.pack(pady=10)

# Fenêtre principale
root = tk.Tk()
root.title("Application")
root.geometry("500x400")
root.configure(bg="#e6f7ff")

# Frame de connexion
login_frame = tk.Frame(root, bg="#e6f7ff")
login_frame.pack(pady=20)

tk.Label(login_frame, text="Connexion", font=("Arial", 18), bg="#e6f7ff").pack(pady=10)

tk.Label(login_frame, text="Nom d'utilisateur:", bg="#e6f7ff").pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack(pady=5)

tk.Label(login_frame, text="Mot de passe:", bg="#e6f7ff").pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Se connecter", command=verify_credentials, bg="#4caf50", fg="white")
login_button.pack(pady=10)

tk.Button(login_frame, text="Créer un compte", command=show_register_page, bg="#2196f3", fg="white").pack(pady=5)

# Frame d'inscription
register_frame = tk.Frame(root, bg="#e6f7ff")

tk.Label(register_frame, text="Inscription", font=("Arial", 18), bg="#e6f7ff").pack(pady=10)

tk.Label(register_frame, text="Nom d'utilisateur:", bg="#e6f7ff").pack(pady=5)
reg_username_entry = tk.Entry(register_frame)
reg_username_entry.pack(pady=5)

tk.Label(register_frame, text="Mot de passe:", bg="#e6f7ff").pack(pady=5)
reg_password_entry = tk.Entry(register_frame, show="*")
reg_password_entry.pack(pady=5)

tk.Label(register_frame, text="Confirmer le mot de passe:", bg="#e6f7ff").pack(pady=5)
reg_confirm_password_entry = tk.Entry(register_frame, show="*")
reg_confirm_password_entry.pack(pady=5)

register_button = tk.Button(register_frame, text="S'inscrire", command=register_user, bg="#4caf50", fg="white")
register_button.pack(pady=10)


tk.Button(register_frame, text="Retour à la connexion", command=show_login_page, bg="#2196f3", fg="white").pack(pady=5)

# Démarrage sur la page de connexion
show_login_page()

# Boucle principale
root.mainloop()
