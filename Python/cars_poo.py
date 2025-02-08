# Classe mère
class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def demarrer_moteur(self):
        return f"Le moteur de la {self.marque} {self.modele} ({self.annee}) démarre."

    def arreter_moteur(self):
        return f"Le moteur de la {self.marque} {self.modele} ({self.annee}) s'arrête."


# Classe fille : Voiture Électrique
class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, annee, capacite_batterie):
        super().__init__(marque, modele, annee)
        self.capacite_batterie = capacite_batterie  # en kWh

    def charger_batterie(self):
        return f"La batterie de la {self.marque} {self.modele} est en charge. Capacité : {self.capacite_batterie} kWh."


# Classe fille : Voiture de Sport
class VoitureSport(Voiture):
    def __init__(self, marque, modele, annee, vitesse_max):
        super().__init__(marque, modele, annee)
        self.vitesse_max = vitesse_max  # en km/h

    def afficher_vitesse(self):
        return f"La vitesse maximale de la {self.marque} {self.modele} est de {self.vitesse_max} km/h."


# Classe fille : Camion
class Camion(Voiture):
    def __init__(self, marque, modele, annee, capacite_chargement):
        super().__init__(marque, modele, annee)
        self.capacite_chargement = capacite_chargement  # en tonnes

    def charger_cargo(self):
        return f"Le camion {self.marque} {self.modele} charge de la marchandise. Capacité : {self.capacite_chargement} tonnes."


# Utilisation des classes
if __name__ == "__main__":
    # Création des objets
    tesla = VoitureElectrique("Tesla", "Model S", 2023, 100)
    ferrari = VoitureSport("Ferrari", "F8 Tributo", 2022, 340)
    volvo = Camion("Volvo", "FH16", 2021, 30)

    # Appel des méthodes
    print(tesla.demarrer_moteur())
    print(tesla.charger_batterie())
    print()

    print(ferrari.demarrer_moteur())
    print(ferrari.afficher_vitesse())
    print()

    print(volvo.demarrer_moteur())
    print(volvo.charger_cargo())
    print(volvo.arreter_moteur())
