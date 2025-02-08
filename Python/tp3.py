class Produit:
    # Variable de classe pour suivre le nombre total de produits
    compteur_produits = 0

    def __init__(self, nom, prix, quantite):
        """
        Constructeur de la classe Produit.
        """
        self.id = Produit.compteur_produits + 1  # Génère un identifiant unique
        self.nom = nom  # Nom du produit
        self.prix = prix  # Prix du produit
        self.quantite = quantite  # Quantité en stock
        Produit.compteur_produits += 1  # Incrémente le compteur global
        print(f"Produit créé : {self}")

    def __str__(self):
        """
        Méthode d'affichage utilisateur.
        """
        return f"[ID: {self.id}] {self.nom} - Prix: {self.prix:.2f}€ - Quantité: {self.quantite}"

    def __repr__(self):
        """
        Méthode de représentation technique pour les développeurs.
        """
        return f"Produit(id={self.id}, nom={self.nom!r}, prix={self.prix}, quantite={self.quantite})"

    def ajuster_quantite(self, quantite):
        """
        Ajuste la quantité en stock du produit.
        """
        self.quantite += quantite
        print(f"Quantité ajustée pour {self.nom}. Nouvelle quantité: {self.quantite}")

    def mettre_a_jour_prix(self, nouveau_prix):
        """
        Met à jour le prix du produit.
        """
        self.prix = nouveau_prix
        print(f"Prix mis à jour pour {self.nom}. Nouveau prix: {self.prix:.2f}€")

    def __del__(self):
        """
        Destructeur de la classe Produit.
        """
        Produit.compteur_produits -= 1  # Décrémente le compteur global
        print(f"Produit supprimé : {self.nom}. Produits restants: {Produit.compteur_produits}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Création de quelques produits
    p1 = Produit("Téléphone", 799.99, 50)
    p2 = Produit("Ordinateur Portable", 1299.99, 30)

    # Affichage des informations des produits
    print(p1)
    print(p2)

    # Ajustement des quantités
    p1.ajuster_quantite(-5)  # Retirer 5 unités du stock
    p2.ajuster_quantite(10)  # Ajouter 10 unités au stock

    # Mise à jour des prix
    p1.mettre_a_jour_prix(749.99)  # Réduction de prix
    p2.mettre_a_jour_prix(1399.99)  # Augmentation de prix

    # Suppression d'un produit
    del p1  # Appelle le destructeur

    # Affichage des informations restantes
    print(f"Produits dans l'inventaire : {Produit.compteur_produits}")
