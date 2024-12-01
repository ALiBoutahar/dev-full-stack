import math

class NombreComplexe:
    def __init__(self, reel, imaginaire):
        """
        Constructeur de la classe NombreComplexe.
        """
        self.reel = reel
        self.imaginaire = imaginaire

    def __str__(self):
        """
        Méthode d'affichage utilisateur.
        """
        return f"{self.reel} {'+' if self.imaginaire >= 0 else '-'} {abs(self.imaginaire)}i"

    def module(self):
        """
        Calcul du module d'un nombre complexe.
        """
        return math.sqrt(self.reel**2 + self.imaginaire**2)

    def __sub__(self, autre):
        """
        Surcharge de l'opérateur - pour la soustraction.
        """
        return NombreComplexe(self.reel - autre.reel, self.imaginaire - autre.imaginaire)

    def __mul__(self, autre):
        """
        Surcharge de l'opérateur * pour la multiplication.
        """
        reel = self.reel * autre.reel - self.imaginaire * autre.imaginaire
        imaginaire = self.reel * autre.imaginaire + self.imaginaire * autre.reel
        return NombreComplexe(reel, imaginaire)

    def __truediv__(self, autre):
        """
        Surcharge de l'opérateur / pour la division.
        """
        if autre.reel == 0 and autre.imaginaire == 0:
            raise ZeroDivisionError("Division par zéro interdite pour les nombres complexes.")
        
        denominateur = autre.reel**2 + autre.imaginaire**2
        reel = (self.reel * autre.reel + self.imaginaire * autre.imaginaire) / denominateur
        imaginaire = (self.imaginaire * autre.reel - self.reel * autre.imaginaire) / denominateur
        return NombreComplexe(reel, imaginaire)

    def __repr__(self):
        """
        Représentation technique pour les développeurs.
        """
        return f"NombreComplexe(reel={self.reel}, imaginaire={self.imaginaire})"


# Partie 3: Tests et Validation
def tests():
    # Création de deux nombres complexes
    z1 = NombreComplexe(3, 4)
    z2 = NombreComplexe(1, -2)

    # Affichage des nombres complexes
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")

    # Calcul et affichage du module
    print(f"Module de z1: {z1.module():.2f}")
    print(f"Module de z2: {z2.module():.2f}")

    # Opérations mathématiques
    print(f"z1 - z2 = {z1 - z2}")
    print(f"z1 * z2 = {z1 * z2}")
    print(f"z1 / z2 = {z1 / z2}")

    # Cas limites
    z3 = NombreComplexe(0, 0)
    z4 = NombreComplexe(5, 0)
    print(f"z4 = {z4}")
    try:
        print(f"z1 / z3 = {z1 / z3}")  # Doit lever une exception
    except ZeroDivisionError as e:
        print(f"Erreur: {e}")

    z5 = NombreComplexe(0, -7)
    print(f"z5 = {z5}")
    print(f"z1 * z5 = {z1 * z5}")


if __name__ == "__main__":
    tests()
