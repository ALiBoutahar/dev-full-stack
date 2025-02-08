class MonObjet:
    # Compteur global d'objets
    compteur_global = 0

    def __init__(self, nom):
        """
        Constructeur de la classe MonObjet.
        """
        self.nom = nom  # Nom de l'objet
        self.compteur_operations = 0  # Compteur d'opérations spécifiques à l'objet
        MonObjet.compteur_global += 1  # Incrémentation du compteur global
        print(f"Objet '{self.nom}' créé. Total d'objets: {MonObjet.compteur_global}")

    def __str__(self):
        """
        Représentation utilisateur de l'objet.
        """
        return f"MonObjet(nom='{self.nom}', opérations={self.compteur_operations})"

    def __repr__(self):
        """
        Représentation technique de l'objet.
        """
        return f"MonObjet(nom={self.nom!r}, compteur_operations={self.compteur_operations})"

    def operation(self):
        """
        Incrémente le compteur d'opérations pour cet objet.
        """
        self.compteur_operations += 1
        print(f"Opération effectuée sur '{self.nom}'. Total d'opérations: {self.compteur_operations}")

    def afficher_statistiques(self):
        """
        Affiche les statistiques de l'objet.
        """
        print(f"Statistiques pour '{self.nom}': {self.compteur_operations} opérations effectuées.")

    def __del__(self):
        """
        Destructeur de la classe MonObjet.
        """
        MonObjet.compteur_global -= 1  # Décrémentation du compteur global
        print(f"Objet '{self.nom}' détruit. Objets restants: {MonObjet.compteur_global}")


# Exemple d'utilisation
if __name__ == "__main__":
    obj1 = MonObjet("Objet1")
    obj1.operation()
    obj1.operation()
    obj1.afficher_statistiques()

    obj2 = MonObjet("Objet2")
    obj2.operation()

    print(obj1)
    print(repr(obj2))

    # Suppression manuelle d'un objet
    del obj1

    # Fin du programme (les destructeurs restants seront appelés automatiquement)
