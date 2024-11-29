import tkinter as tk
from tkinter import messagebox

# Fonction de vérification
def verify_credentials():
    username = username_entry.get()
    password = password_entry.get()
    
    # Login et mot de passe
    valid_username = "admin"
    valid_password = "1234"
    
    if username == valid_username and password == valid_password:
        open_welcome_window()
    else:
        messagebox.showerror("Erreur", "Login ou mot de passe incorrect")

# Fonction pour ouvrir la fenêtre de bienvenue
def open_welcome_window():
    root.withdraw()  # Masquer la fenêtre principale
    welcome_window = tk.Toplevel()
    welcome_window.title("Bienvenue")
    welcome_window.geometry("300x200")
    
    welcome_label = tk.Label(welcome_window, text="Welcome!", font=("Arial", 16))
    welcome_label.pack(pady=50)
    
    close_button = tk.Button(welcome_window, text="Fermer", command=welcome_window.destroy)
    close_button.pack(pady=10)

# Fenêtre principale
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Widgets pour le login
username_label = tk.Label(root, text="Nom d'utilisateur:")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

password_label = tk.Label(root, text="Mot de passe:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Se connecter", command=verify_credentials)
login_button.pack(pady=10)

# Boucle principale
root.mainloop()
